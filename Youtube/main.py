import streamlit as st
import time 
from googleapiclient.discovery import build
import pandas as pd
import datetime
from dateutil import parser
import isodate
import pymongo
import mysql.connector


header = st.container()
channels = st.container()
playlists = st.container()


with header:
    st.title('Youtube Data Harvesting Project')
    

# Taking the channel details from youtube by using youtube api  
with channels:
    st.subheader('Channel')
    get_channels,channel_run = st.columns([10,1])
    # getting the channel id as a input from the user by using streamlit 
    get_input = get_channels.text_input('Enter your Youtube id  ')
    user_input = get_input

# channel_ids=['UCc8_LsRYszE9-T-BkIcS7jw','UCpNUYWW0kiqyh0j5Qy3aU7w']
channel_ids = [user_input,]

api_key = 'AIzaSyCYfsYTMGua8jL8paIoIy5biijwBRYQpE4'
api_service_name = "youtube"
api_version = "v3"
youtube = build( api_service_name, api_version, developerKey=api_key ) 

# This function is to get all details from the respective youtube channel
def get_channels(youtube,channel_ids):
    channel_data = []
    
    channel_request = youtube.channels().list(
    part = 'snippet,contentDetails,statistics',
    id = ','.join(channel_ids)
    )
    channel_response = channel_request.execute()

    for c_item in channel_response['items']:
        data = {
            'channelId':c_item['id'],
            'channelName':c_item['snippet']['title'],
            'subscribers':c_item['statistics']['subscriberCount'],
            'views':c_item['statistics']['viewCount'],
            'description':c_item['snippet']['description'],
            'playlistId':c_item['contentDetails']['relatedPlaylists']['uploads']
        }
        channel_data.append(data)
    return channel_data

channels_list = get_channels(youtube,channel_ids)

# Loading channel details from youtube to mongodb database
client = pymongo.MongoClient('mongodb://localhost:27017')
mongo_db = client['youtube']

channel = mongo_db['channel']
channel.drop()
channel = mongo_db['channel']

with channels:
    if st.button(' Run '):
        channel.insert_many(channels_list)
        progress_bar = st.progress(0)

        for i in range(100):
            time.sleep(.01)
            progress_bar.progress(i+1)

        progress_bar.empty()

        st.success('Loaded successfully!')

        document = []
        for doc in channel.find():
            document.append(doc)

        st.write(document)


#-----------------------------------------------------------------------------------------------------------------

with playlists:
    st.subheader('Playlist')
    get_playlists,playlist_run = st.columns([10,1])
    # getting the playlist id as a input from the user by using streamlit 
    get_user_input = get_playlists.text_input('Enter your Playlist id  ')
    get_playlist_id = str(get_user_input)

playlist_id = get_playlist_id

def get_videos(youtube,playlist_id):
    
    video_ids = []

    request = youtube.playlistItems().list(
        part = 'snippet,contentDetails',
        playlistId = playlist_id,
        maxResults = 50
    )
    response = request.execute()
    
    for item in response['items']:
        data={'videoId':item['contentDetails']['videoId'],'channelId':item['id']}
        video_ids.append(data)
    next_page_token = response.get('nextPageToken')
    
    while next_page_token is not None:
        request = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = playlist_id,
        maxResults = 50,
        pageToken = next_page_token
        )

        response = request.execute()

        for item in response['items']:
            data={'videoId':item['contentDetails']['videoId'],'channelId':item['id']}
            video_ids.append(data)
        next_page_token = response.get('nextPageToken')
        
    return video_ids

video_ids = get_videos(youtube,playlist_id)

with playlists:
    if st.button(' P_Run '):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(.01)
            progress_bar.progress(i+1)
        progress_bar.empty()
        st.success('Loaded successfully!')

        st.write(video_ids)
    

