import praw
from tokens import ID, SECRET, AGENT
from random import randint

def fact():
  reddit = praw.Reddit(client_id='euKbwQfzEm5wCQ',
                       client_secret='pLhl3cHO95mGhgq22M3H4p-wfQc',
                       user_agent='getmotiv-alexa by /u/devishsh')

  getmotiv = reddit.subreddit('GetMotivated').random()
  topic = getmotiv.title[ getmotiv.title.find(']') + 1 :]

  while 'Discussion' in getmotiv.title or len(topic) == 0:
    getmotiv = reddit.subreddit('GetMotivated').random()
    topic = getmotiv.title[getmotiv.title.find(']'):]

  # getmotiv.comments.replace_more(limit=0)
  # comments = getmotiv.comments.list()
  # fact = comments[randint(0,99) % len(comments)]

  # topic = clean(topic)
  # factText = clean(fact.body)

  return topic

def find_link(s):
  x = s.find(']')
  if x == -1:
    return s
  y = s[x:].find(')')
  return find_link(s[:x] + s[x+y:])

def find_http(s):
  x = s.find('http://')
  if x == -1:
    return s
  y = s[x:].find(')')
  return find_http(s[:x] + s[x+y:])

def find_www(s):
  x = s.find('www.')
  if x == -1:
    return s
  y = s[x:].find(')')
  return find_www(s[:x] + s[x+y:])

def clean(s):
  s = find_link(s)
  s = find_http(s)
  s = find_www(s)
  return s

if __name__ == '__main__':
  print fact()