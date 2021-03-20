from time import time
from random import randint
from sys import stdout, stdin


def printf(text, divider="\n"): #faster print
    text = str(text)
    stdout.write(text + divider)


def input(prompt="\n"): #faster input
    stdout.write(prompt)
    return stdin.readline().strip()


defaults = {"adding": ("+", 10000, 100000), "subtracting": ("-", 10000, 100000), "multiplying": ("*", 10, 100), "dividing": ("/", 1000, 10000)} #command: (operator, start, end)


def calculating(command, start=None, end=None):
    if start == None or end == None:  #in case optional parameters aren't passed
        start = defaults[command][1]
        end = defaults[command][2]
    num1 = randint(start, end)
    num2 = randint(start, end)
    if command in ("subtracting", "dividing"): #In case we get negative or number between 0 and 1
        num1, num2 = max(num1, num2), min(num1, num2)
    printf(f"{num1} {defaults[command][0]} {num2} = ")
    return round(eval(f"{num1} {defaults[command][0]} {num2}"), 2)


def helping():
    print("""
Created for people, who want to calculate fast, and without a calculator. @DevBubo
Commands:
adding
subtracting
multiplying
dividing

You can exit of any mode by typing "Cancel".
You can also edit the range of numbers, that will appear in your calculation by typing a command,
you want and adding range, e.g "adding 50000 5000000"
If you want this message to reappear, type "cancel".
""")


command = "cancel"
command_stopper = False
while True:
    if command == "cancel": #pops up help menu
        helping()
        command = input("What would you like to do? ").split()
    else:
        if command[0] in defaults:
            if len(command) == 3:
                result = calculating(command[0], int(command[1]), int(command[2]))
            elif len(command) == 1:
                result = calculating(command[0])  #prints equation, and saves its result to result
            else:
                raise Exception("Invalid format, your command should be in format 'command' or in format 'command start end', e.g adding or adding 50000 500000.")
            timerStart = time() #starting timing, how long does it take you to solve the equation
            yourResult = input("Enter your result: ")
            if yourResult == "cancel":
                command = "cancel"
            while yourResult not in (str(result), "cancel"):
                if yourResult == "cancel":
                    command = "cancel"
                    break
                yourResult = input("Enter your result: ")
            print(f"{round(time() - timerStart, 2)}s")
        else:
            raise Exception("Invalid format")
