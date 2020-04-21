"""Environment Variables Configuration Module"""
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")

FILE_PATH = os.getenv("FILE_PATH")
SERIAL_PORT = os.getenv("SERIAL_PORT")
DEBUG = os.getenv("DEBUG")

def check_enviroment():
    """Checks whether any .env environment variables are missing"""
    assert(SERIAL_PORT), "Serial Port missing on .env"