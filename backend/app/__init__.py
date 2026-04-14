from flask import Flask
from dotenv import load_dotenv

def create_app():
    # 1. Load .env variables
    load_dotenv()

    # 2. Create the Flask instance
    app = Flask(__name__)

    # 3. Return the app
    return app

    



