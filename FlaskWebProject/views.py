"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, Flask, request, jsonify, json, abort
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'chat_main.html',
        title='Welcome to PEACH Chatbot!',
        year=datetime.now().year,
    )

@app.route('/chat_main')
def chat_main():
    return render_template(
        'chat_main.html',
        title='Welcome to PEACH Chatbot!',
        year=datetime.now().year,
    )

@app.route("/showConsent")
def showConsent():
    return render_template("consent.html")

@app.route("/chatBot")
def chatBot():
    return render_template("chatBot.html")

@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/api/chatBot", methods=['POST'])
def postChat():
    return NLP(request.get_data())

def NLP(t):
    return "You wrote " + t

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
