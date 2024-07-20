import streamlit as st
import yt_dlp
import os
from pathlib import Path

st.title('YouTube Video Downloader For Assam Mamaya')

# Input for YouTube video link
link = st.text_input('Enter YouTube video link:')

if st.button('Download'):
    if link:
        try:
            # Get the path to the user's Downloads folder
            path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
            
            # Ensure the save path exists
            if not os.path.exists(path_to_download_folder):
                os.makedirs(path_to_download_folder)
            
            st.write(f"Downloading video from: {link}")
            
            ydl_opts = {
                'outtmpl': os.path.join(path_to_download_folder, '%(title)s.%(ext)s'),
                'format': 'mp4'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            st.success(f'Video downloaded successfully to {path_to_download_folder}!')
        except Exception as e:
            st.error(f"Error while downloading the video: {e}")
    else:
        st.warning('Please enter a valid YouTube link.')

# Display the downloaded videos
st.header('Downloaded Videos')
path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
if os.path.exists(path_to_download_folder):
    videos = os.listdir(path_to_download_folder)
    for video in videos:
        st.write(video)
else:
    st.write("The Downloads folder does not exist.")
