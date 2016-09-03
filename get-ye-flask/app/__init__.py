from flask import Flask

app = Flask(__name__)

# this import has to be after the above line to avoid circular imports
from app import views
