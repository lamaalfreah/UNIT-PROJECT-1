import cohere
import os
from dotenv import load_dotenv
from ai_services.ai_services import save

load_dotenv()
api_key: str | None = os.environ.get("COHERE_API_KEY")
if not api_key:
    raise ValueError("COHERE_API_KEY is missing from environment variables.")
co = cohere.Client(api_key)

def summarize(text: str, username: str, topic: str) -> str:
    """
    Generates a summary for the given text using Cohere's Summarization API, 
    saves the summary to a user/topic-specific folder, and opens the saved file.

    Args:
        text (str): The input text to be summarized.
        username (str): The name of the user (used to organize saved summaries).
        topic (str): The topic under which the summary will be saved.

    Returns:
        str: The generated summary if successful, otherwise a failure message.
    """
    try:
        response = co.summarize(text=text)
        file_path: str = save(username, topic, response.summary, "summary")
        os.system(f"open '{file_path}'") 
        return response.summary
    except Exception as e:
        print("An unexpected error occurred while communicating with Cohere API.")
        print(e)

    return "Summarization failed :( Please try again later."