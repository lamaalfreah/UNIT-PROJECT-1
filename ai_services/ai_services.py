import os
from datetime import datetime

class AIServices:
    def __init__(self, base_dir="data") -> None:
        self.base_dir = base_dir

    def save(self, username: str, topic: str, text: str, label: str = "transcript") -> str:
        """
        Save text in a structured folder under data/{username}/{topic}.
        
        :param username: The user name
        :param topic: The topic name
        :param text: The content to save
        :param label: A label like 'transcript', 'summary', 'question'
        """
        base_path = os.path.join(self.base_dir, username, topic, f"{label}s")
        os.makedirs(base_path, exist_ok=True)

        # Count existing files with this label
        existing_files = [f for f in os.listdir(base_path) if f.startswith(f"{label}_")]
        file_number = len(existing_files) + 1

        # Add timestamp to filename
        # timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # filename = f"{label}_{file_number}_{timestamp}.txt"

        filename = f"{label}_{file_number}.txt"
        file_path = os.path.join(base_path, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"The text was saved in: {file_path}")
        return file_path 