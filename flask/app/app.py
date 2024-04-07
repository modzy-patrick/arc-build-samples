from flask import Flask, request, jsonify,send_file
from flask_cors import CORS
import dotenv
from datetime import datetime

dotenv.load_dotenv()

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello_world():
    """
    hello world
    """
    return "Hello from gng-copilot sample backend" 

if __name__ == '__main__':
    app.run(debug=True)
