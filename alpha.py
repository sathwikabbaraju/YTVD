# import os
# import streamlit as st
# import yt_dlp

# def download_youtube_audio(video_url, output_folder="downloads"):
#     try:
#         # Create output directory if it doesn't exist
#         if not os.path.exists(output_folder):
#             os.makedirs(output_folder)

#         # yt-dlp options
#         ydl_opts = {
#     'format': 'bestaudio/best',
#     'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
#     'cookiefile': '/Users/sathwik/VISUAL STUDIO CODE/Streamlit/YTVD/cookies.txt',  # Specify the path to your cookies file
# }


#         with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#             info_dict = ydl.extract_info(video_url, download=True)
#             title = info_dict.get('title', None)
#             mp3_filename = os.path.join(output_folder, f"{title}.mp3")

#         return mp3_filename
#     except Exception as e:
#         st.error(f"Error: {e}")
#         return None

# st.title("YouTube to MP3 Converter")

# video_url = st.text_input("Enter YouTube video URL:")
# if st.button("Download MP3"):
#     if video_url:
#         mp3_file = download_youtube_audio(video_url)
#         if mp3_file and os.path.exists(mp3_file):
#             with open(mp3_file, "rb") as file:
#                 st.download_button(
#                     label="Download MP3",
#                     data=file,
#                     file_name=os.path.basename(mp3_file),
#                     mime="audio/mpeg"
#                 )
#     else:
#         st.warning("Please enter a valid YouTube URL.")


import os
import streamlit as st
import yt_dlp
import tempfile

def download_youtube_content(video_url, download_type, output_folder="downloads"):
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Set yt-dlp options based on download type
        if download_type == "Audio (MP3)":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'cookiefile': '/path/to/your/cookies.txt',  # Update this path if needed
            }
            file_ext = 'mp3'
        else:  # Video
            ydl_opts = {
                'format': 'mp4',
                'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
                'cookiefile': '/Users/sathwik/VISUAL STUDIO CODE/Streamlit/YTVD/cookies.txt',  # Update this path if needed
            }
            file_ext = 'mp4'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=True)
            title = info_dict.get('title', 'downloaded_video')
            file_path = os.path.join(output_folder, f"{title}.{file_ext}")

        return file_path
    except Exception as e:
        st.error(f"Error: {e}")
        return None

st.title("YouTube Video/Audio Downloader")

video_url = st.text_input("Enter YouTube video URL:")
download_type = st.radio("Select download type:", ("Video (MP4)", "Audio (MP3)"))

if st.button("Download"):
    if video_url:
        file_path = download_youtube_content(video_url, download_type)
        if file_path and os.path.exists(file_path):
            with open(file_path, "rb") as file:
                st.download_button(
                    label=f"Download {download_type}",
                    data=file,
                    file_name=os.path.basename(file_path),
                    mime="video/mp4" if download_type == "Video (MP4)" else "audio/mpeg"
                )
    else:
        st.warning("Please enter a valid YouTube URL.")
