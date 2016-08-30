"""
The flask application package.
"""

from flask import Flask
import os

sys.path.append("FlaskWebProject/chatbot")

app = Flask(__name__)
app.secret_key=os.urandom(24)

import FlaskWebProject.views
