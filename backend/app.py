import os
from flask import Flask
from dotenv import load_dotenv 

# Load variables from the .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def hello_world():
    return 'Hello, World'

# Run the app if this script is executed directly
if __name__ == '__main__':

# Returns '5000' if 'PORT' is not set
    port = os.getenv('PORT', '5000')
    app.run (port=port, debug=True)