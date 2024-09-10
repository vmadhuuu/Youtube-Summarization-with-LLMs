from yt_dlp import YoutubeDL
import os
import re

def sanitize_filename(filename):
    # Replace special characters with underscores or remove them
    return re.sub(r'[^\w\s-]', '', filename).strip().replace(' ', '_')

def download_video(url, save_path="data/"):
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s')  # Save the video with its title as the filename
    }
    
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', None)
        video_extension = info_dict.get('ext', 'mp4')
        
        # Sanitize the filename to remove special characters and spaces
        sanitized_title = sanitize_filename(video_title)
        original_video_path = os.path.join(save_path, f"{video_title}.{video_extension}")
        sanitized_video_path = os.path.join(save_path, f"{sanitized_title}.{video_extension}")

        # Rename the file with the sanitized title if necessary
        if os.path.exists(original_video_path):
            os.rename(original_video_path, sanitized_video_path)
    
    print(f"Downloaded video: {sanitized_video_path}")
    return sanitized_video_path