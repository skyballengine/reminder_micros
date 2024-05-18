#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects json from client, needs to json.dump() to deserialize 
#

import time
import zmq
import json
from reminder import Reminder
from datetime import datetime

# take in data dict already been json loaded back to python
def create_reminder(data):
    print(data, end="\n")
    new_reminder = Reminder(data["name"], data["dtime"], data["amount"])
    return new_reminder

def convert_from_json(comm_in):
    message_to_dict = json.loads(str(message))
    print(message_to_dict)
    print(type(message_to_dict))

    pass

def convert_to_json():
    pass

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

while True:
    #  Wait for next request from client
    # message = json.loads(socket.recv())
    # converted_message = json.dump(message)
    message = socket.recv()
    print()
    print(f"Received request: {message}")
    print(type(message), end="\n")
    print()
    # print(converted_message)
    message_to_dict = json.loads(message)

    # message_to_dict = dict(message_to_string)
    print(message_to_dict)
    print(type(message_to_dict))
    print()
    reminder = create_reminder(message_to_dict)
    print(reminder)

    date_string = reminder.get_datetime()
    reminder_name = reminder.get_name()
    print(reminder_name)
    print(date_string, end="\n")

    response = "Your reminder: " + reminder_name + " for: " + date_string + " has been created and is viewable in your calendar!"
    # print(type("Your reminder: " + reminder_name + " for: " + date_string + " has been created and is viewable in your calendar!"))
    encoded_response = response.encode("UTF-8")
    print(type(response))
    print(type(encoded_response))
    
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(encoded_response)
