# This is the server to communicate with Chris's Jobs Board
# Binds REP socket to tcp://localhost/5555
# Will receive job data that will include the name and datetime
# Then will respond with a reminder object.

import time
import zmq
from reminder import Reminder
import socket

hostname = socket.gethostname()
ip_addr = socket.gethostbyname(hostname)
test_addr = "localhost"
PORT=5555

print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + ip_addr)

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(f"tcp://{test_addr}:{PORT}")

while True:
    # wait for requests from clients
    message = socket.recv()
    if message == "Hello":
        socket.send(b"Hello yourself")
    print(f"Received a request: {message}")

    # name, dtime = message

    # # create a reminder object
    # reminder = Reminder(name, dtime)
    # time.sleep(1)

    # send reminder object to client
    # socket.send(reminder)


