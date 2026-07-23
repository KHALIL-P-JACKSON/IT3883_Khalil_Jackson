# Program Name: Sprint1.py
# Course: IT3883/Section W01
# Student Name: Khalil Jackson
# Assignment Number: Final Exam
# Due Date: 07/23/2026
# Purpose: For this assignment I will write a python program that will take the input of a sentence of currency and convert it into a USD value.


# Take input
Sentence = input("Enter a sentence of currency: ")

#Split the sentence into words
words = Sentence.split()

Total = 0

# Iterate through the words and calculate the total value
for i in range(len(words)):
    # Check if the current word is a number
    if words[i].isdigit():
        coin = words[i+1]

        # Check the type of coin
        if coin == "penny" or coin == "pennies":
            Total += 0.01 * int(words[i])
        elif coin == "nickel" or coin == "nickels":
            Total += 0.05 * int(words[i])
        elif coin == "dime" or coin == "dimes":
            Total += 0.10 * int(words[i])
        elif coin == "quarter" or coin == "quarters":
            Total += 0.25 * int(words[i])
        elif coin == "dollar" or coin == "dollars":
            Total += 1.00 * int(words[i])

# Print the total value
print(f"Total value: ${Total:.2f}")