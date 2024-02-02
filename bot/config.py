import os
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('venv')
load_dotenv(dotenv_path=dotenv_path)

BOT_TOKEN = os.getenv("BOT_TOKEN")
