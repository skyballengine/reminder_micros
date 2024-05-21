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

d. The microservice will be available upon request, at which point it will be running on my local machine and we will coordinate so that at a specified time I will provide the ip address and port so the socket will be open and available to communicate.

e. I will be available at our agreed upon time to ensure that the microservice is functioning at the specified ip address and port, should any issues arise, we can work through it.

![Model] (https://github.com/skyballengine/reminder_micros/blob/c74da72b9c52cf64c6dacd2c91549b15ef3a216d/Reminder%20Microservice.png)





