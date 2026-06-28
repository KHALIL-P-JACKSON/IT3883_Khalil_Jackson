# Program Name: Assignment4-B.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 4
# Due Date: 06/27/2026
# Purpose: This program will be a client that will connect to server A and send data.
# I used the module power point and chatGPT to learn how to set up a server and client.


import socket

# Create a socket object for server B
server_B = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to server A
server_B.connect(('localhost', 8080))

# Send a message to server A
message = "Hello from server B!"
server_B.sendall(message.encode('utf-8'))

# receive a response from server A and respond back with the same message in uppercase
response = server_B.recv(1024)
print(f"Received response: {response.decode('utf-8')}") 
response = response.decode('utf-8')
response = response.upper()
server_B.sendall(response.encode('utf-8'))

server_B.close()