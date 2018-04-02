from flask import Flask

app = Flask(__name__)

# Import the apis
from app import apis
