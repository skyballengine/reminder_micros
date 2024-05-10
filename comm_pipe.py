# This is the server to communicate with Chris's Jobs Board
# Binds REP socket to tcp://localhost/5555
# Will receive job data that will include the name and datetime
# Then will respond with a reminder object.

PORT=5555

import time
import zmq
from reminder import Reminder
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://{IPAddr}:{PORT}")
# print(context.get(zmq.IDENTITY))

while True:
    # wait for requests from clients
    message = socket.recv()
    print(f"Received a request: {message}")
    #TODO deconstruct request to get the name and datetime
    name, dtime = message

    # create a reminder object
    reminder = Reminder(name, dtime)
    time.sleep(1)

    # send reminder object to client
    socket.send(reminder)


