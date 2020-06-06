from flask import Flask, request
from controller import controller
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-key'
