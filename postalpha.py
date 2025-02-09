import os
import streamlit as st
import yt_dlp
import tempfile

st.title('YouTube Video/Audio Downloader')

# Input for YouTube video link
link = st.text_input('Enter YouTube video URL:')
download_type = st.radio('Select download type:', ('Video (MP4)', 'Audio (MP3)'))

if st.button('Download'):
    if link:
        try:
            # Create a temporary directory
            with tempfile.TemporaryDirectory() as tmpdirname:
                st.write(f"Downloading {download_type.lower()} from: {link}")
                
                # Set yt-dlp options based on download type
                if download_type == 'Audio (MP3)':
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': os.path.join(tmpdirname, '%(title)s.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                    file_ext = 'mp3'
                else:  # Video (MP4)
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
                        'outtmpl': os.path.join(tmpdirname, '%(title)s.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegVideoConvertor',
                            'preferedformat': 'mp4',
                        }],
                    }
                    file_ext = 'mp4'

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])
                
                # Find the downloaded file
                downloaded_files = os.listdir(tmpdirname)
                if downloaded_files:
                    downloaded_file = os.path.join(tmpdirname, downloaded_files[0])
                    # Provide a download link to the user
                    with open(downloaded_file, "rb") as file:
                        st.download_button(
                            label=f"Download {download_type}",
                            data=file,
                            file_name=downloaded_files[0],
                            mime='audio/mpeg' if file_ext == 'mp3' else 'video/mp4'
                        )
                
                st.success(f'{download_type} downloaded successfully!')
        except Exception as e:
            st.error(f"Error while downloading the {download_type.lower()}: {e}")
    else:
        st.warning('Please enter a valid YouTube link.')
