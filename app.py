from flask import Flask, request
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-key'
