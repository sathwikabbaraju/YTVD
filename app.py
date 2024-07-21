import streamlit as st
import yt_dlp
import os
import tempfile

st.title('YouTube Video Downloader For Assam Mamaya')

# Input for YouTube video link
link = st.text_input('Enter YouTube video link:')

if st.button('Download'):
    if link:
        try:
            # Create a temporary directory
            with tempfile.TemporaryDirectory() as tmpdirname:
                st.write(f"Downloading video from: {link}")
                
                ydl_opts = {
                    'outtmpl': os.path.join(tmpdirname, '%(title)s.%(ext)s'),
                    'format': 'mp4'
                }
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                
                # Find the downloaded file
                downloaded_files = os.listdir(tmpdirname)
                if downloaded_files:
                    downloaded_file = os.path.join(tmpdirname, downloaded_files[0])
                    # Provide a download link to the user
                    with open(downloaded_file, "rb") as file:
                        btn = st.download_button(
                            label="Download Video",
                            data=file,
                            file_name=downloaded_files[0],
                            mime='video/mp4'
                        )
                
                st.success(f'Video downloaded successfully!')
        except Exception as e:
            st.error(f"Error while downloading the video: {e}")
    else:
        st.warning('Please enter a valid YouTube link.')

# Display the downloaded videos
st.header('Downloaded Videos')
st.write("Download videos will be available after clicking the download button.")
