# Program Name: Assignment4-A.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 4
# Due Date: 06/27/2026
# Purpose: This program will be a server that will receive data from server B and send back a response.
# I used the module power point and chatGPT to learn how to set up a server and client.


import socket

# Create a socket object for server A
server_A = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_A.bind(('localhost', 8080))
server_A.listen(1)
conn, addr = server_A.accept()
print(f"Connection from {addr} has been established!")

# Receive data from server B 
data = conn.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

# Insert a prompt and send back a response to server B
prompt = input("What would you like to send back to server B? ")
conn.sendall(prompt.encode('utf-8'))

data = conn.recv(1024)
print(f"Received data: {data.decode('utf-8')}")

conn.close()