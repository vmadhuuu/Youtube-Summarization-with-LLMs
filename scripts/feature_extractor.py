import os
import torch
import librosa
import cv2
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image
import speech_recognition as sr
from transformers import Wav2Vec2Processor, Wav2Vec2Model

import os
import torch
import librosa
from transformers import Wav2Vec2Processor, Wav2Vec2Model

def extract_audio_features(video_path):
    # Sanitize file paths with quotes to handle spaces or special characters
    audio_path = video_path.replace(".mp4", ".wav")
    sanitized_audio_path = f'"{audio_path}"'
    sanitized_video_path = f'"{video_path}"'

    # List files in the data directory to confirm the file exists
    print(f"Files in data directory: {os.listdir('data/')}")
    print(f"Video path: {video_path}")
    
    # Use FFmpeg to extract the audio
    command = f'ffmpeg -i {sanitized_video_path} -q:a 0 -map a {sanitized_audio_path}'
    print(f"Running command: {command}")
    os.system(command)
    
    # Verify if the .wav file exists
    if not os.path.exists(audio_path):
        raise FileNotFoundError(f"Audio file not created: {audio_path}")
    
    # Load the audio file using librosa
    y, sr = librosa.load(audio_path, sr=16000)
    
    # Process the audio with Wav2Vec2 for feature extraction
    processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base")
    model = Wav2Vec2Model.from_pretrained("facebook/wav2vec2-base")
    
    inputs = processor(y, sampling_rate=sr, return_tensors="pt")
    with torch.no_grad():
        features = model(**inputs).last_hidden_state
    return features

# Extract Visual Features
def extract_visual_features(video_path):
    resnet_model = models.resnet50(pretrained=True)
    resnet_model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    visual_features = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 30 == 0:  # Process every 30th frame
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            img_t = transform(img)
            batch_t = torch.unsqueeze(img_t, 0)
            with torch.no_grad():
                features = resnet_model(batch_t)
                visual_features.append(features.squeeze(0).numpy())

    cap.release()
    print(f"Extracted {len(visual_features)} visual feature vectors.")
    return visual_features

# Extract Text Transcripts
def extract_text_transcripts(video_path):
    audio_path = video_path.replace(".mp4", ".wav")
    os.system(f"ffmpeg -i {video_path} -q:a 0 -map a {audio_path}")
    
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(audio_path)

    with audio_file as source:
        audio_data = recognizer.record(source)

    try:
        transcript = recognizer.recognize_google(audio_data)
        print(f"Transcript: {transcript[:100]}...")  # Print first 100 characters of transcript
        return transcript
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
