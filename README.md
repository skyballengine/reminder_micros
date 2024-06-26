Reminder Microservice

1. Request Data:

A request in the form of a dictionary that includes the following keys and values that will become the data members of the Reminder object.

\*All keys and values are strings
"name": "_name_",
"date": "_date",
"amount": "\_amount_"

Example:
test_request_dict = {
"name": "Phone bill",
"date": "12-12-2024",
"amount": "250.00"
}

2. Receive Data:

Data recieved is a string that contains a confirmation message that includes the name, date, and amount of the Reminder.
The message also states that the Reminder has been stored in the database.

- Reference test_comm_client.py as that is client program to request data

3. Mitigation Plan

a. The Reminder Microservice was created for Abdulellah's Bill Tracking App.

b. The microservice is complete.

c. There are no issues currently.

d. The microservice will be available upon request, at which point it will be running on my local machine and we will coordinate so that at a specified time I will provide the ip address and port so the socket will be open and available to communicate.

e. I will be available at our agreed upon time to ensure that the microservice is functioning at the specified ip address and port, should any issues arise, we can work through it.

f. If problems arise, I will be available via our Slack channel to figure out a solution.

g. Nothing additional at this time.

UML Sequence Diagram
! [Model] (https://github.com/skyballengine/reminder_micros/blob/e4949e1f07743eaafce58f3ac0fa7b11354e3fc5/Reminder%20Microservice.png)

