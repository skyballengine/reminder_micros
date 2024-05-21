#
#   ZeroMQ Server in Python
#   Binds REP socket to tcp://*:5555
#   Expects json from client, needs to json.dump() to deserialize 
#

import time
import zmq
import json
from reminder import Reminder
from datetime import datetime
from pprint import pprint

# take in data dict already been json loaded back to python
def create_reminder(data):
    print(data, end="\n")
    new_reminder = Reminder(data["name"], data["date"], data["amount"])
    return new_reminder


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://localhost:5555")

while True:
    #  Wait for next request from client
    # message = json.loads(socket.recv())
    # converted_message = json.dump(message)
    message = socket.recv_json()
    pprint(f"Received request: {message}")
    pprint(type(message))

    # Create Reminder object using dict from client
    reminder = create_reminder(message)
    pprint(reminder)
    pprint(type(reminder))

    reminder_date = reminder.get_date()
    reminder_name = reminder.get_name()
    reminder_amount = reminder.get_amount()

    response = f"Your reminder: {reminder_name} for {reminder_amount} on {reminder_date} has been created and is viewable in your calendar!"
    # print(type("Your reminder: " + reminder_name + " for: " + reminder_date + " has been created and is viewable in your calendar!"))
    encoded_response = response.encode("UTF-8")
    
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(encoded_response)
