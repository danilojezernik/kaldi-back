import os

from dotenv import load_dotenv

load_dotenv()
PORT = os.getenv('PORT')
API_KEY = os.getenv('API_KEY')