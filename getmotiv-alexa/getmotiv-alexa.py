import logging
from random import randint
from flask import Flask, json, render_template
from flask_ask import Ask, request, session, question, statement, context, audio, current_stream
import praw
from getmotiv import fact

app = Flask(__name__)
ask = Ask(app, "/")
logger = logging.getLogger()
logging.getLogger('flask_ask').setLevel(logging.INFO)


@ask.launch
def launch():
  return fact()

@ask.intent('AnotherIntent')
def another():
  return fact()

@ask.intent('AMAZON.HelpIntent')
def help():
  speech = "Say \"Tell me a fact\" to hear a fact. Say \"Tell me more\" to hear another fact. "
  return question(speech)

@ask.session_ended
def session_ended():
  return "{}", 200

if __name__ == '__main__':
  app.run(debug=True)
