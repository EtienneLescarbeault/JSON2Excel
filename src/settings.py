import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
GEOCODIO_API_KEY = os.environ.get("GEOCODIO_API_KEY")
