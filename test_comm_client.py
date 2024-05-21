import time
import zmq
import socket
import json
from datetime import datetime
from pprint import pprint

PORT=5555
hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
pprint("Your Computer Name is:" + hostname)
pprint("Your Computer IP Address is:" + ip_addr)


test_request_dict = {
    "name": "Phone bill", 
    "date": "12-12-2024", 
    "amount": "250.00"
}
print(type(test_request_dict))

#
#   ZeroMQ Client in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends a reminder parameters to microservice and receives back a Reminder object
#   Needs to jsonloads() thus serializing the reminder parameters as strings to json, 
#   then send that json to the server (reminder microservice)

context = zmq.Context()

#  Socket to talk to server
pprint("Connecting to Reminder microservice....")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


socket.send_json(test_request_dict)



#  Get the reply.
message = socket.recv().decode()

pprint(f"Received reply: {str(message)} ")