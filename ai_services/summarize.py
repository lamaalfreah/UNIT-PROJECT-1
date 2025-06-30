import cohere
import os
from dotenv import load_dotenv
load_dotenv()

def summarize(text):
    co = cohere.Client(os.environ.get("COHERE_API_KEY"))
    response = co.summarize(
        text=text,
    )
    print(response.summary)

