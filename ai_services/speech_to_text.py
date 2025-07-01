import whisper
import os
import yt_dlp
from ai_services.ai_services import save

def download_youtube_audio(url: str, username: str, topic: str) -> str:
    """
    Download audio from YouTube and save it in user's topic folder.
    
    :param url: YouTube video URL
    :param username: User name for folder structure
    :param topic: Topic under the user
    :return: Path to downloaded mp3 file
    """
    try:
        base_path = os.path.join("data", username, topic, "audio")
        os.makedirs(base_path, exist_ok=True)

        # Count existing files with this label
        existing_files = [f for f in os.listdir(base_path) if f.startswith("audio_")]
        file_number = len(existing_files) + 1
        filename = f"audio_{file_number}.mp3"
        file_path = os.path.join(base_path, filename)
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': file_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return file_path
    
    except Exception as e:
        print("Failed to download audio from YouTube.")
        print(e)
        return ""

def convert_audio_to_text(source: str, username: str, topic: str, is_youtube: bool = False) -> str:
    """
    Converts audio from YouTube or file path to text using Whisper.
    
    :param source: YouTube URL or path to audio file
    :param is_youtube: Set to True if source is a YouTube link
    :return: Transcribed text
    """
    try:
        # Load Whisper model
        model = whisper.load_model("base")  

        if is_youtube:
            print("Downloading audio from YouTube...")
            audio_path = download_youtube_audio(source, username, topic)
            if not audio_path or not os.path.exists(audio_path):
                raise FileNotFoundError("Audio download failed or file not found.")
       
        else:
            audio_path = source
            if not os.path.exists(audio_path):
                raise FileNotFoundError("Audio file not found.")
            
        print("Transcribing audio...")
        result = model.transcribe(audio_path)
        file_path = save(username, topic, result["text"], "transcript")
        os.system(f"open '{file_path}'") 
        return result["text"]
    
    except Exception as e:
        print("Error during audio transcription.")
        print(e)
        return "Transcription failed. Please try again."