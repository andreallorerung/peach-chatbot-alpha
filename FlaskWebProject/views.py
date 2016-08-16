"""
Routes and views for the flask application.
"""


from datetime import datetime, timedelta
from flask import Flask, request, render_template, jsonify, json, abort, session,g, redirect, url_for
import simplejson as json
from flask.ext.sqlalchemy import SQLAlchemy
import pyodbc
import urlparse
from FlaskWebProject import app
import os
import ctypes
import uuid

#import subprocess



#connecting to database
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};''Server=tcp:peach-chatbot.database.windows.net,1433;''Database=peach-chatbot;''Uid=chatbot@peach-chatbot;Pwd=Peach-2016;')

#opening a cursor and query to check data in registration table
cursor = conn.cursor()
cursor.execute('SELECT email, PIN FROM registration WHERE DOB = \'1989-08-11\'')

row=cursor.fetchone()
while row:
    print row
    row = cursor.fetchone()

#cursor.callproc('sp_createUser',(_pin,_dob))

#data = cursor.fetchall()


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


#@app.route("/showConsent")
#def showConsent():
#    return render_template("consent.html")

@app.route("/chatBot")
def chatBot():
        return render_template("chatBot.html")

@app.route("/search")
def search():
        return render_template("search.html")

#@login_required #require users to be logged in to access
@app.route("/chatBrain")
def chatBrain():
        return render_template("chatBrain.html")

@app.route("/ehna")
def ehna():
    if g.user:
        return render_template("ehna.html")

    return render_template("chatBot.html")

@app.route("/api/chatBot", methods=['POST'])
def sendConcerns():
    return NLP(request.get_data())
    #return json.loads('[{"name":"respiratory", "value":"3"},{"name":"mouth","value":"3"}]')
    #NLP(request.get_data())
    #result =simplejson.loads('json_arr')
    #initialConcerns= result[{'name':value}]
    #return initialConcerns
    #for element in result ['name']:
    #    return element



@app.route("/api/chatBot/chat", methods=['POST'])
def postChat():
    return NLP (request.get_data())

def NLP(t):

    return t


#build data in correct format to query db
def build_date_string(login_data):
    return login_data['year'][0] + '-' + login_data['month'][0] + '-%02d' % int(login_data['day'][0])

#perform sql query to validate login details
def check_credentials(pin, dob):
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM registration WHERE PIN = %s AND DOB = \'%s\'' % (pin, dob))

    row=cursor.fetchone()
    while row:
        return row

#sign in route and create user session
@app.route("/signIn", methods =['POST'])
def signIn():
    login_data = urlparse.parse_qs(request.get_data())
    dob = build_date_string(login_data)
    if str(check_credentials(login_data['pinNumber'][0], dob)) == 'None':
        return ctypes.windll.user32.MessageBoxA(0, "Your login details were incorrect. Please try again.", "Incorrect Login Details", 1)
    #session.pop('user', None)
    userid= uuid.uuid4()
    session['user'] = userid
    print userid
    return redirect(url_for('ehna'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user =session['user']
        session.permanent = True
        flask_app.permanent_session_lifetime = timedelta(minutes=1)
        session.modified = True
        if timedelta(minutes=0):
            return logout()

    #return 'not timed out yet'

@app.route('/logout')
def logout():
    return redirect(url_for('chat_main'))
    session.pop('user', None)
    print 'Logged out.'



@app.route('/contact')
def contact():
    #"""Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
#    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
)
