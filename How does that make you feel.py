# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 20:00:29 2020

@author: ralls
"""

'''
Challenge:
  Work on getting responses
  See what happens when you pass the appropriate arguments to format_response()
  
'''
from random import randrange
from reference import *
import re

def remove_punc(user_response):
  user_response = user_response.replace(".", "")
  user_response = user_response.replace("!", "") 
  #user_response = user_response.lower()
  return user_response


''' The function you write to match patterns must return two values:

    1 .The (first) key from the dictionary whose pattern was a match
    2. The MatchObject resulting from re.match()
'''

def get_match(user_response):
  # loop thru psychobabble_patterns to find the match
  for key, value in psychobabble_patterns.items():
    # Match the value and the user response
    match = re.search(value, user_response)
    # If there is a match, then return the key and the MatchObject
    if match != None:
        return match, key
  # If there are no matches in the whole loop, then return None, MatchObject
  return match, None


def get_response(key):
  # Find the response options for that key
  # Return a random one
  # if the key is not None, then get response options
  if key != None:
    response_number = randrange(len(psychobabble_responses[key]))
    response = psychobabble_responses[key][response_number]
  # if the key is None, then get "else" response options
  elif key == None:
    response_number = randrange(len(psychobabble_responses['else']))
    response = psychobabble_responses['else'][response_number]
  return response

user_response = input("Hello, How are you doing today? ")

while user_response != 'quit':
  user_response = remove_punc(user_response)
  match, key = get_match(user_response)
  response = get_response(key) 
  eliza_response = format_response(match, response)
  user_response = input(eliza_response)
  
if user_response == 'quit':
  match, key = get_match(user_response)
  response = get_response(key) 
  eliza_response = format_response(match, response)
  print(eliza_response)
      
      
      
      
      