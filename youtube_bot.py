'''
Youtube bot for pulling channel data
'''
import configparser
import json
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

    def run(self):
        '''
        @brief Main bot functionality
        '''
        print('Pulling data')
        channel_info = self.pull_channel_stats('ethoslab')
        print(f'Info on channel: {channel_info}')
    
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
