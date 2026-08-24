import os
from dotenv import load_dotenv

load_dotenv()

SESSION_ID = os.getenv("INSTAGRAM_SESSION_ID")
if not(SESSION_ID):
    raise ValueError("Missing INSTAGRAM_SEESSION_ID in .env file")
