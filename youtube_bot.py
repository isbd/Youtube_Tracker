'''
Youtube bot for pulling channel data
'''
import configparser
import math
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from googleapiclient.discovery import build

class YoutubeBot():
    '''
    @brief Youtube bot class to pull data
    '''
    def __init__(self, config):
        '''
        @brief Init to assign api token and connect youtube

        @param config Config file to pull api_token from 
        '''
        self.token = config['youtube']['api_token']
        self.youtube = build('youtube', 'v3', developerKey=self.token)
        self.channel_list = ['ethoslab']
        self.channel_list_by_id = ['']

    def run(self):
        '''
        @brief Main bot functionality
        '''
        print('Pulling data')
        channel_info = self.pull_channel_stats(self.channel_list[0])
        print(f'Info on channel: {channel_info}')
        user_id = self.pull_channel_id(self.channel_list[0])
        video_list = self.get_uploaded_videos(user_id, 10)
        print(f'Video list: {video_list}')
        print(f'Entries: {len(video_list)}')
        print(self.pull_captions(video_list[0]['snippet']['resourceId']['videoId']))
    
    def pull_channel_stats(self, username):
        '''
        @brief Creates request for specified channel statistics

        @param username Username of channel to search stats for

        @return Returns dict of statistics or False if failed connection
        '''
        request = self.youtube.channels().list(
            part='statistics',
            forUsername=username
        )
        result = self.handle_request(request)
        if result:
            return result['items'][0]['statistics']
        return False

    def pull_channel_id(self, username):
        '''
        @brief Pull's id reference of channel based off username

        @param username Username of channel to pull id

        @return Returns id or false if failed connection
        '''
        request = self.youtube.channels().list(
            part = 'id',
            forUsername = username
        )
        result = self.handle_request(request)
        if result:
            return result['items'][0]['id']
        return False

    def get_uploaded_videos(self, channel_id, number_to_search):
        '''
        @brief Pull's number of upload videos from channel id

        @param channel_id Channel to pull uploaded videos from

        @param number_to_search Number of videos to pull

        @return Returns List of uploaded videos
        '''
        pages_to_iterate = math.ceil(number_to_search / 50) - 1
        playlist = self.pull_uploads_playlist_reference(channel_id)
        video_list = []

        if playlist:
            request = self.youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist,
                maxResults=number_to_search
            )
            result = self.handle_request(request)
            video_list.extend(result['items'])
            for _ in range(0, pages_to_iterate):
                number_to_search -= 50
                #Out of pages
                if 'nextPageToken' not in result:
                    break
                request = self.youtube.playlistItems().list(
                    part="snippet",
                    playlistId=playlist,
                    maxResults=number_to_search,
                    pageToken=result['nextPageToken']
                )
                result = self.handle_request(request)
                video_list.extend(result['items'])
            return video_list
        return False

    def pull_uploads_playlist_reference(self, channel_id):
        '''
        @brief Pull's uploaded playlist

        @param channel_id Channel to pull uploaded videos from

        @return Returns playlist of uploaded videos or False if failed
        '''
        request = self.youtube.channels().list(
            part="contentDetails",
            id=channel_id,
            fields="items(contentDetails/relatedPlaylists/uploads,id)"
        )
        result = self.handle_request(request)
        if result:
            return result['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        return False

    @staticmethod
    def pull_captions(video_id):
        '''
        @brief Pulls captions for specified video id

        @param video_id Video Id reference for pulling captions

        @return Returns caption details in dictionary list including text, 
            start, duration or False if no captions
        '''
        try:
            caption_dictionary = YouTubeTranscriptApi.get_transcript(video_id)
        except TranscriptsDisabled as exception:
            return False
        return caption_dictionary

    @staticmethod
    def handle_request(request):
        '''
        @brief Executes request, handles if error occurs

        @param request Http object for request

        @return Returns request execution result or false if failed
        '''
        try:
            return request.execute()
        except Exception as exception:
            print(f'Issue with request, {exception}')
            return False

config = configparser.ConfigParser()
config.read('config.ini')
youtube_bot = YoutubeBot(config)
youtube_bot.run()
