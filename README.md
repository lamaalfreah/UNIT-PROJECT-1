# AI Lecture Toolkit 🤖

A smart, interactive CLI application that helps users extract value from educational audio content. Whether you're a student or a researcher, this tool allows you to **transcribe audio**, **summarize long text**, and **generate intelligent questions** — all within a command-line interface.

---

## 📌 Project Requirements (Satisfied)

- ✅ Fully interactive through the Command Line Interface (CLI)
- ✅ Pythonic and modular code structure
- ✅ Organized into packages/modules
- ✅ Version-controlled with Git and GitHub

---

## 🚀 Features & User Stories

### 👤 As a user, I can:
- Register a new account or log in.
- Create topic-based folders to organize my work.
- Transcribe audio files or YouTube links into text.
- Summarize long text using AI.
- Generate short, relevant questions from any passage.
- Browse all saved content grouped by topic.
- Open and delete files directly from the terminal.

---

## 🧪 Usage

Once you run the project, you'll see a menu:

```
1. 🎧 Transcribe audio  
2. 📝 Summarize text  
3. ❓ Generate questions  
4. 📁 Browse your content  
5. ❌ Exit  
```

---

## 🧩 Project Structure

```
.
├── main.py                     # Main CLI logic
├── auth.py                     # Login and registration functions
├── browse.py                   # File navigation and deletion
├── ai_services/
│   ├── summarize.py            # AI-based summarization
│   ├── question_generator.py   # AI question generator
│   └── speech_to_text.py       # Whisper audio transcription
├── data/                       # User data saved here
│   └── [username]/[topic]/
└── requirements.txt            # Python dependencies
```

---

## 🔧 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # On Mac/Linux
   venv\Scripts\activate           # On Windows
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your environment variables in `.env`**
   ```
   COHERE_API_KEY=your_cohere_api_key
   ```

5. **Run the app**
   ```bash
   python main.py
   ```

---

## 📦 Dependencies

- [Whisper](https://github.com/openai/whisper) – for audio transcription  
- [Cohere API](https://cohere.ai) – for summarization and question generation  
- [Rich](https://github.com/Textualize/rich) – for a beautiful CLI interface  
- `yt-dlp` – for downloading YouTube audio  
- `python-dotenv` – for loading API keys securely  

---