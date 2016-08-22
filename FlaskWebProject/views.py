"""
Routes and views for the flask application.
"""


from datetime import datetime, timedelta
from flask import Flask, request, render_template, jsonify, json, abort, session,g, redirect, url_for
import simplejson as json
from flask_sqlalchemy import SQLAlchemy
import pyodbc
import urlparse
from FlaskWebProject import app
import os
import ctypes
import uuid
from chatbot.botinterface import bot_builder, bot_rivescript
from chatbot.concerns import concern_factory, drive_conversation
from chatbot.messagelog import message
from chatbot.messagelog.message import Message
from chatbot.messagelog.conversation_logging import ConversationLogger
from chatbot.messagelog.conversation import Conversation


#instantiate bot
bot = bot_rivescript.BotRivescript(brain='FlaskWebProject/chatbot/brain')

userid1=uuid.uuid4()
userid = str(userid1)

#connecting to database
#conn = pyodbc.connect('Driver={SQL Server};''Server=tcp:peach-chatbot.database.windows.net,1433;''Database=peach-chatbot;''Uid=chatbot@peach-chatbot;Pwd=Peach-2016;')

#opening a cursor and query to check data in registration table
#cursor = conn.cursor()
#cursor.execute('SELECT email, PIN FROM registration WHERE DOB = \'1989-08-11\'')

#row=cursor.fetchone()
#while row:
#    print row
#    row = cursor.fetchone()

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
@app.route("/msgChat")
def msgChat():
        return render_template("msgChat.html")

@app.route("/ehna")
def ehna():
    if g.user:
        return render_template("ehna.html")

    return render_template("chatBot.html")

@app.route("/api/chatBot", methods=['POST'])
def sendConcerns():
    concerns = (request.get_data())
    qs = dict( (k, v if len(v)>1 else v[0] )
           for k, v in urlparse.parse_qs(concerns).iteritems() )
    build_concernsList(qs)
    #initialConcerns = json.loads(concerns)
    #print initialConcerns[0]['name']
    #initialConcerns= urlparse.parse_qs(concerns)
    #build_concernsList(initialConcerns)
    #userConcerns = build_concerns(initialConcerns)
    #print initialConcerns
    #return concerns
    #print json.dumps(initialConcerns)
    welcome = 'Bot: Thank you for submitting your concerns. Type "set glob" to begin dicussing them.'
    return welcome
    #print concerns['respiratory',value]
    #print concerns['respiratory']
    #return jsonify('respiratory')

    #return jsonify(name=name,value=value)
    #print json.loads(concerns)
    #return concerns
    #print urlparse.parse_qs(concerns)
    userConcernsModel = concern_factory.UserConcernsFactory.getUserConcerns(userid)
    userConcernsModel.setInitialUserConcerns(qs)
    #HERE CALL DISTRESS CONVERSATION DRIVER TO PUT CONCERNS INTO RIGHT MODEL FOR bot
    #return 'ok'
    #return redirect(url_for('msgChat'))


    #return json.loads('[{"name":"respiratory", "value":"3"},{"name":"mouth","value":"3"}]')
    #NLP(request.get_data())
    #result =simplejson.loads('json_arr')
    #initialConcerns= result[{'name':value}]
    #return initialConcerns
def build_concernsList(qs):
    #concerns = "{"
    for k,v in qs.items():
        qs[k] = int(v) #v = int(v)
        #concerns +=  k + ":"  +  v + ","
        #concerns += '{0} : {1}, '.format(k, v)
        #print concerns
    print qs

    #concerns += "}"
    #return concerns

#def build_concerns(initialConcerns):
#    return initialConcerns['name'] +  int(initialConcerns['value'])

@app.route("/api/chatBot/chat", methods=['POST'])
def postChat():
    content=request.get_data()
    print content
    print userid
    #return content
    #data sent through will be 'content'
    userMessage = Message(userid,content)
    ConversationLogger.logUserMessage(userMessage)
    msg = bot.reply(userMessage)
    ConversationLogger.logSystemReplyForUser(msg,userid)
    #_retrieveConversationFor(userid)
    #return conversation
    #print conversation
    print msg
    #return redirect(url_for('chat_main'))
    return msg

    #print reply
    #print msg
    #return msg

    #return NLP (request.get_data())

def NLP(t):

    return urlparse.parse_qsl(t)


#build data in correct format to query db
def build_date_string(login_data):
    return login_data['year'][0] + '-' + login_data['month'][0] + '-%02d' % int(login_data['day'][0])

#perform sql query to validate login details
#def check_credentials(pin, dob):
#    cursor = conn.cursor()
#    cursor.execute('SELECT email FROM registration WHERE PIN = %s AND DOB = \'%s\'' % (pin, dob))

#    row=cursor.fetchone()
#    while row:
#        return row

#sign in route and create user session
@app.route("/signIn", methods =['POST'])
def signIn():
    #login_data = urlparse.parse_qs(request.get_data())
    #dob = build_date_string(login_data)
    #if str(check_credentials(login_data['pinNumber'][0], dob)) == 'None':
    #    return ctypes.windll.user32.MessageBoxA(0, "Your login details were incorrect. Please try again.", "Incorrect Login Details", 1)


    session['user'] = userid
    #print userid
    return redirect(url_for('ehna'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user =session['user']
        session.permanent = True
        app.permanent_session_lifetime = timedelta(minutes=1)
        session.modified = True
        if timedelta(minutes=0):
            return logout()

    #return 'not timed out yet'

@app.route('/logout')
def logout():
    return redirect(url_for('chat_main'))
    session.pop('user', None)
    session.set_cookie('user',expires=0)
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



#String concerns = "{";
#for (Map.Entry<String, Integer> entry : concerns.entrySet()){
 # concerns += entry.getKey() + ":" + entry.getValue() + ",\n";
#}
#concerns = concerns.subString (0, concerns.lengh -1 );
#concerns += "}"
