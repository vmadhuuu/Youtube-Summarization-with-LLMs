from scripts.video_downloader import download_video
from scripts.inference import summarize_video
from scripts.utils import check_directory

def main(video_url):
    # Create necessary directories
    check_directory("data/")
    
    # Step 1: Download YouTube video
    video_path = download_video(video_url)
    
    # Step 2: Summarize the video
    summary = summarize_video(video_path)
    print(f"Video Summary: {summary}")

if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ")
    main(video_url)
