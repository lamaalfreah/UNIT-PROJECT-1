import cohere
import os
from dotenv import load_dotenv
from ai_services.ai_services import AIServices

load_dotenv()
api_key: str | None = os.environ.get("COHERE_API_KEY")
if not api_key:
    raise ValueError("COHERE_API_KEY is missing from environment variables.")
co = cohere.Client(api_key)

def generate_questions(text: str, username: str, topic: str, num_questions=3):
    """
    Generates a list of questions from the given text using Cohere's chat API,
    saves them to a user/topic folder, and opens the file.

    Args:
        text (str): The input text to base the questions on.
        username (str): User folder name.
        topic (str): Topic folder name.
        num_questions (int): Number of questions to generate.

    Returns:
        str: The generated questions.
    """

    prompt = f"""
    Generate {num_questions} clear, short, and relevant questions in English or Arabic 
    (based on the input) from the following passage. 
    Do not include answers. Only list the questions, each one numbered on a new line.

    {text}

    """
    try:
        response = co.chat(
            message=prompt,
            model="command-r-plus", 
            temperature=0.7
        )
        content: str = response.text.strip()
        file_path: str = AIServices().save(username, topic, content, "questions")
        os.system(f"open '{file_path}'") 
        return content
    
    except Exception as e:
        print("An unexpected error occurred while communicating with Cohere API.")
        print(e)

    return "Failed to generate questions due to a network issue or API error :( \n Please check your connection or try again later."