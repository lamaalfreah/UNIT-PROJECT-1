import whisper
import os
import yt_dlp
from ai_services.ai_services import save
def download_youtube_audio(url: str, output_path: str = "temp_audio") -> str:
    """Download audio from YouTube and return the mp3 file path using yt-dlp."""
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file = os.path.join(output_path, "youtube_audio.%(ext)s")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_file,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return os.path.join(output_path, "youtube_audio.mp3")


def convert_audio_to_text(source: str, username: str, topic: str, is_youtube: bool = False) -> str:
    """
    Converts audio from YouTube or file path to text using Whisper.
    
    :param source: YouTube URL or path to audio file
    :param is_youtube: Set to True if source is a YouTube link
    :return: Transcribed text
    """
    # Load Whisper model
    model = whisper.load_model("base")  

    if is_youtube:
        print("Downloading audio from YouTube...")
        audio_path = download_youtube_audio(source)
    else:
        audio_path = source

    print("Transcribing audio...")
    result = model.transcribe(audio_path)
    file_path = save(username, topic, result["text"], "transcript")
    os.system(f"open '{file_path}'") 
    return result["text"]