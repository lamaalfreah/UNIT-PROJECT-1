from rich.console import Console
from rich.prompt import Prompt, Confirm
from ai_services.summarize import summarize
from ai_services.speech_to_text import convert_audio_to_text
from ai_services.question_generator import generate_questions
from auth import register, login
from browse import browse_user_content

console = Console()

def welcome() -> str:
    """
    Prompts the user to log in or register.

    Returns:
        str: The username of the authenticated or newly registered user.
    """
    while True:
        choice: str = input("Please select one of the available options: [login / reg]: ").lower()

        if choice == "login":
            username: str = login()
            if username:  
                return username
            else:
                print("Returning to registration...\n")
                username: str = register()
                return username

        elif choice == "reg":
            username: str = register()
            return username

        else:
            print("❗ Invalid input. Please type 'login' or 'reg'.")

def main() -> None:
    """
    The main function of the AI Lecture Toolkit.
    Provides a menu of AI services including transcription, summarization, and question generation.
    """
    console.print("[bold cyan]📌 Welcome to the AI Lecture Toolkit![/bold cyan]\n")

    username: str = welcome()

    while True:
        console.print("\n[bold green]Choose a service:[/bold green]")
        console.print("1. 🎧 Transcribe audio")
        console.print("2. 📝 Summarize text")
        console.print("3. ❓ Generate questions")
        console.print("4. 📁 Browse your content")
        console.print("5. ❌ Exit")

        choice: str = Prompt.ask("Your choice", choices=["1", "2", "3", "4", "5"])

        if choice == "1":
            topic: str = Prompt.ask("📚 Enter the topic")
            is_youtube: bool = Confirm.ask("Is the audio from YouTube?")
            if is_youtube:
                url: str = Prompt.ask("Paste the YouTube URL")
                text: str = convert_audio_to_text(url, username, topic, is_youtube=True)
            else:
                path: str = Prompt.ask("Enter local audio file path")
                text: str = convert_audio_to_text(path, username, topic)

            if text and not text.startswith("Transcription failed"):
                next_action_flow(text, username, topic, from_step="transcription")

        elif choice == "2":
            topic: str = Prompt.ask("📚 Enter the topic")
            text: str = Prompt.ask("Paste the text to summarize")
            summarize(text, username, topic)
            next_action_flow(text, username, topic, from_step="summary")


        elif choice == "3":
            topic: str = Prompt.ask("📚 Enter the topic")
            text: str = Prompt.ask("Paste the text to generate questions from")
            generate_questions(text, username, topic)
            next_action_flow(text, username, topic, from_step="questions")

        elif choice == "4":
            browse_user_content(username)

        elif choice == "5":
            console.print("[bold yellow]Goodbye! 👋[/bold yellow]")
            break

def next_action_flow(original_text: str, username: str, topic: str, from_step: str) -> None:
    """
    Guides the user to additional actions based on the last completed step.
    
    Args:
        original_text (str): The original text resulting from transcription or user input.
        username (str): The current user's username.
        topic (str): The topic folder to store generated content.
        from_step (str): The last completed step (e.g., "summary", "questions", "transcription").
    """
    if from_step == "summary":
        generate: bool = Confirm.ask("❓ Do you want to generate questions from the original text?")
        if generate:
            generate_questions(original_text, username, topic)
            next_action_flow(original_text, username, topic, from_step="questions")

    elif from_step == "questions":
        summarize_text: bool = Confirm.ask("📝 Do you want to summarize the original text?")
        if summarize_text:
            summarize(original_text, username, topic)
            next_action_flow(original_text, username, topic, from_step="summary")

    elif from_step == "transcription":
        while True:
            console.print("\n[bold green]What would you like to do next?[/bold green]")
            console.print("1. 📝 Summarize the text")
            console.print("2. ❓ Generate questions")
            console.print("3. 🔁 Return to main menu")

            choice: str = Prompt.ask("Your choice", choices=["1", "2", "3"])

            if choice == "3":
                break
            elif choice == "1":
                summarize(original_text, username, topic)
                next_action_flow(original_text, username, topic, from_step="summary")
            elif choice == "2":
                generate_questions(original_text, username, topic)
                next_action_flow(original_text, username, topic, from_step="questions")

if __name__ == "__main__":
    main()