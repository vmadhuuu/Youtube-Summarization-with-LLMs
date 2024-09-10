from scripts.feature_extractor import extract_audio_features, extract_text_transcripts
from scripts.model import SummarizationModel

def summarize_video(video_path):
    # Extract features
    audio_features = extract_audio_features(video_path)
    text_transcripts = extract_text_transcripts(video_path)
    
    # Initialize summarization model
    model = SummarizationModel()
    
    # Generate summary (using the transcript text)
    summary = model.generate_summary(text_transcripts)
    print(f"Summary: {summary}")
    return summary

if __name__ == "__main__":
    video_path = "data/sample_video.mp4"
    summarize_video(video_path)
