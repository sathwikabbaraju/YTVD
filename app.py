import streamlit as st
import yt_dlp
import os

st.title('YouTube Video Downloader For Assam Mamaya')

# Input for YouTube video link
link = st.text_input('Enter YouTube video link:')

if st.button('Download'):
    if link:
        try:
            # Define the save path to the "Downloads" folder
            folder_path = os.path.expanduser("~/Downloads")
            
            # Ensure the save path exists
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            st.write(f"Downloading video from: {link}")
            
            ydl_opts = {
                'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
                'format': 'mp4'
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            
            st.success(f'Video downloaded successfully to {folder_path}!')
        except Exception as e:
            st.error(f"Error while downloading the video: {e}")
    else:
        st.warning('Please enter a valid YouTube link.')

# Display the downloaded videos
st.header('Downloaded Videos')
folder_path = os.path.expanduser("~/Downloads")
if os.path.exists(folder_path):
    videos = os.listdir(folder_path)
    for video in videos:
        st.write(video)
else:
    st.write("The Downloads folder does not exist.")
