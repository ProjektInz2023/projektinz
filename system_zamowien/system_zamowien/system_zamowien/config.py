"""
Configuration file that contains constant variables.
"""

import os
from dotenv import load_dotenv
load_dotenv()

# Database connector variables
DB_URL = os.getenv("DB_URL")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")