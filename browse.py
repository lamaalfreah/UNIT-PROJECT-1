import os
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm

console = Console()

def browse_user_content(username: str) -> None:
    """
    Browse and manage user-generated content by listing topics and files.

    Allows the user to select a topic, then displays a table of all associated files 
    (including files in subfolders). The user can choose to open or delete a file.

    Args:
        username (str): The name of the user whose content should be browsed.

    Returns:
        None
    """
    user_path: str = os.path.join("data", username)
    if not os.path.exists(user_path):
        console.print(f"[red]No data found for user {username}[/red]")
        return

    # List available topic folders under the user's directory
    topics = []  
    for d in os.listdir(user_path):  
        full_path: str = os.path.join(user_path, d)  
        if os.path.isdir(full_path):  
            topics.append(d) 

    if not topics:
        console.print("[yellow]No topics found.[/yellow]")
        return
    
    # Display list of topics with numbering
    console.print("\n[bold green]Available Topics:[/bold green]")
    for i, topic in enumerate(topics, 1):
        console.print(f"{i}. {topic}")

    # Ask user to select a topic number
    topic_choice: str = Prompt.ask("Select a topic number", choices=[str(i) for i in range(1, len(topics)+1)])
    selected_topic: str = topics[int(topic_choice) - 1]

    topic_path: str = os.path.join(user_path, selected_topic)

    # Collect files (including those in subfolders)
    # files: List[Tuple[str, str, str]] = [] --> (label, filename, full_path)
    files = []
    for root, _, filenames in os.walk(topic_path):
        for filename in filenames:
            if filename.startswith("."):
                continue  # Ignore hidden files like .DS_Store
            label = os.path.basename(root) if root != topic_path else "main"
            files.append((label, filename, os.path.join(root, filename)))

    if not files:
        console.print("[yellow]No files found in this topic.[/yellow]")
        return

    # Display table
    table = Table(title=f"📂 Files in {selected_topic}", show_lines=True)
    table.add_column("Index", style="cyan", justify="right")
    table.add_column("Type", style="magenta")
    table.add_column("Filename", style="white")

    for idx, (label, filename, _) in enumerate(files, 1):
        table.add_row(str(idx), label, filename)

    console.print(table)

    # Ask user to select a file to open or cancel
    file_choice = Prompt.ask("Enter file number to open or '0' to cancel", choices=[str(i) for i in range(len(files)+1)])
    if file_choice == "0":
        return
    
    # Open the selected file
    file_path = files[int(file_choice)-1][2]
    os.system(f"open '{file_path}'")  

    # Ask whether to delete the file
    if Confirm.ask("\n🗑️ Do you want to delete this file?"):
        os.remove(file_path)
        console.print(f"[bold red]✅ {file_path} deleted successfully.[/bold red]")