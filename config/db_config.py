from databases import Database
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
metadata = create_engine(DATABASE_URL)
