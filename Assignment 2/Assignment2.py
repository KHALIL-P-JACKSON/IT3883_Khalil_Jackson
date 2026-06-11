# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Lab 2
# Due Date: 06/19/2026
# Purpose: This program takes input of students their grades and averages them highest to lowest
# I used ChatGPT to learn how to take all inputs in at once using sys and to learn how to use sort and lambda

import sys


def grade_averager(student_list):
    split_list = student_list.split()
    name = split_list[0]
    del split_list[0]
    grades = [int(i) for i in split_list]
    grade_average = sum(grades)/len(grades)

    return (name, grade_average)


raw_grades = sys.stdin.read().strip()
students = raw_grades.split("\n")

results = []

for student in students:
    results.append(grade_averager(student.strip()))

results.sort(key=lambda x: x[1], reverse=True)

for name, avg in results:
    print(f"{name}: {avg}")


