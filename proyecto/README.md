# Gym Assistant Bot

A simple Streamlit-based chatbot interface for gym and fitness assistance.

## Features
- Streamlit web UI for chat
- Easy to extend for AI or rule-based gym assistant logic

## Project Structure
- `proyecto/app/app.py`: Main Streamlit app
- `proyecto/config.yaml`: Configuration file
- `proyecto/requirements.txt`: Python dependencies
- `proyecto/data/Gym_dream.pdf`: Example data (PDF)
- `.gitignore`: Files/folders to ignore in git

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/JulianaYS/Assistant-Gym.git
   cd gym-assistant-bot/proyecto
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Run the app:**
   ```sh
   streamlit run app/app.py
   ```

## Commit Style
This project uses [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for commit messages. Example:

```
feat: add chat interface to Streamlit app
fix: correct typo in requirements.txt
```

## License
MIT
