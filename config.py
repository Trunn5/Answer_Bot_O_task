import os
from dotenv import load_dotenv
from pathlib import Path

# Переменные из окружения в файле "venv"
dotenv_path = Path('venv')
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
SHEET_ID = os.getenv("SHEET_ID")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
