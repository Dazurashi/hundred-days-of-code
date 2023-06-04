'''
The classic FizzBuzz program solution
'''

numbers = [*range(1, 101)]

for number in numbers:
    if number % 15 == 0: #You could check for both 3 and 5, but there's no need because 15 is the smallest number which is divisible by both
        print(f"{number} FizzBuzz")
    elif number % 3 == 0:
        print(f"{number} Fizz")
    elif number % 5 == 0:
        print(f"{number} Buzz")
    else:
        print(number)