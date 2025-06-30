import whisper
import os
import yt_dlp

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


def convert_audio_to_text(source: str, is_youtube: bool = False) -> str:
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
    return result["text"]

def save_transcript(username: str, topic: str, text: str):
    """
    Save transcribed text in a user/topic folder.
    
    :param username: User's name
    :param topic: Topic selected by user (
    :param text: The transcribed text
    """
    base_path = os.path.join("data", username, topic)
    os.makedirs(base_path, exist_ok=True)

    # Count existing files to avoid overwriting
    existing_files = [f for f in os.listdir(base_path) if f.startswith("transcript_")]
    file_number = len(existing_files) + 1

    file_path = os.path.join(base_path, f"transcript_{file_number}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"The text was saved in: {file_path}") 