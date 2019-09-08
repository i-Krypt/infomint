from flask import Flask
from .config import DevConfig

#init app
app = Flask(__name__)

#Setting up config
app.config.from_object(DevConfig)

from app import views