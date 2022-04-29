'''
Youtube bot for pulling channel data
'''
import configparser
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

    def run(self):
        '''
        @brief Main bot functionality
        '''
        print('Pulling data')
        channel_info = self.pull_channel_stats(self.channel_list[0])
        print(f'Info on channel: {channel_info}')
        user_id = self.pull_channel_id(self.channel_list[0])
        video_list = self.get_video_data(user_id, 30)
        print(f'Info on videos: {video_list}')
    
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

    def get_video_data(self, channel_id, number_to_search):
        '''
        @brief Pull's upload videos from channel id

        @param channel_id Channel to pull uploaded videos from

        @param number_to_search Number of videos to pull

        @return Returns video's json or false if failed connection
        '''
        playlist = self.pull_uploads_playlist(channel_id)
        if playlist:
            request = self.youtube.playlistItems().list(
                part="snippet",
                playlistId=playlist,
                maxResults=number_to_search
            )
            return self.handle_request(request)
        return False

    def pull_uploads_playlist(self, channel_id):
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
