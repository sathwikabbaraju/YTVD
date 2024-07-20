import streamlit as st
import yt_dlp
import os

st.title('YouTube Video Downloader For Assam Mamaya')

# Input for YouTube video link
link = st.text_input('Enter YouTube video link:')
# Input for download folder
folder_path = st.text_input('Enter download folder path:')

if st.button('Download'):
    if link and folder_path:
        try:
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
            
            st.success(f'Video downloaded successfully!')
        except Exception as e:
            st.error(f"Error while downloading the video: {e}")
    else:
        st.warning('Please enter both a valid YouTube link and a download folder path.')

# Display the downloaded videos
if folder_path:
    st.header('Downloaded Videos')
    if os.path.exists(folder_path):
        videos = os.listdir(folder_path)
        for video in videos:
            st.write(video)
    else:
        st.write("The specified folder path does not exist.")

        