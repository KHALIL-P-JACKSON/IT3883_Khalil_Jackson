# Program Name: Assignment5.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 5
# Due Date: 07/5/2026
# Purpose: For this assignment you will write a Python program to create and interact with a database. You are given a file containing temperature readings for each day of the week.
# Using ChatGPT to initally set up teh database and the cursor. I used my local model to then learn how to read the input file and insert the data into the database. 

import sqlite3

#Create a connection to the database and create a cursor object
conn = sqlite3.connect('temperature_readings.db')
cursor = conn.cursor()


#create a table to store the temperature readings
cursor.execute('''
CREATE TABLE IF NOT EXISTS temperature_readings (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)''')


#read the temperature readings from the input file and insert them into the database
with open('C:\\Users\\Khalil Jackson\\School\\IT3883_Khalil_Jackson\\Asssignent 5\\Assignment5input.txt', 'r') as file:
    for line in file:
        day, temperature = line.strip().split()
        cursor.execute('INSERT INTO temperature_readings (Day_Of_Week, Temperature_Value) VALUES (?, ?)', (day, float(temperature)))


#calculate the average temperature for Sunday and Thursday
Sunday_Average = 0 
Thursday_Average = 0

cursor.execute("SELECT Temperature_Value FROM temperature_readings WHERE Day_Of_Week = 'Sunday'")
rows = cursor.fetchall()
for temp in rows:
    Sunday_Average += temp[0]

Sunday_Average /= len(rows)

cursor.execute("SELECT Temperature_Value FROM temperature_readings WHERE Day_Of_Week = 'Thursday'")
rows = cursor.fetchall()    
for temp in rows:
    Thursday_Average += temp[0] 

Thursday_Average /= len(rows)


#print the average temperature for Sunday and Thursday
print(f"Average temperature for Sunday: {Sunday_Average:.2f}")
print(f"Average temperature for Thursday: {Thursday_Average:.2f}")

Sun_Thurs_Average = (Sunday_Average + Thursday_Average) / 2
print(f"Average temperature for Sunday and Thursday: {Sun_Thurs_Average:.2f}")

conn.commit()
conn.close()