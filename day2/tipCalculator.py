'''
This program will ask the user for the total bill.
Then it will ask which percentage tip the user would like to give.
After that it will ask how many people will split the bill.
Finally the program will tell how much each person should pay in 2 decimal accuracy.
'''

print("Welcome to the tip claculator")

total_bill = input("What was the total bill? $")
tip = "1." + input("What persentage tip would you like to give? ")
people = input("How many people are splitting the bill?")

pay = round(float(total_bill) * float(tip) / int(people), 2)

print(f"Your total amount for each person is ${pay}")
