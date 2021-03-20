from time import time
from random import randint
from sys import stdout, stdin


def printf(text, divider="\n"): #faster print
    text = str(text)
    stdout.write(text + divider)


def input(prompt="\n"): #faster input
    stdout.write(prompt)
    return stdin.readline().strip()


def adding(start=10000, end=100000):
    num1 = randint(start, end)
    num2 = randint(start, end)
    printf(f"{num1} + {num2} = ", "")
    return num1 + num2


def subtracting(start=10000, end=100000):
    num1 = randint(start, end)
    num2 = randint(start, end)
    printf(f"{num1} - {num2} = ", "")
    return num1 - num2


def multiplying(start=10, end=100):
    num1 = randint(start, end)
    num2 = randint(start, end)
    printf(f"{num1} * {num2} = ", "")
    return num1 * num2


def dividing(start=1000, end=10000):
    num1 = randint(start, end)
    num2 = randint(start, end)
    printf(f"{max(num1, num2)} / {min(num1, num2)} = ", "")
    return num1 / num2

defaults = {"adding": ("+", 10000, 100000), "subtracting": ("-", 10000, 100000), "multiplying": ("*", 10, 100), "dividing": ("/", 1000, 10000)} #command: (operator, start, end)
def calculating(command, start=None, end=None):
    if start == None or end == None:
        start = defaults[command][1]
        end = defaults[command][2]
    num1 = randint(start, end)
    num2 = randint(start, end)
    if command in ("subtracting", "dividing"): #In case we get negative or number between 0 and 1
        num1, num2 = max(num1, num2), min(num1, num2)
    printf(f"{num1} {defaults[command][0]} {num2} = ", "")
    return round(eval(f"{num1} {defaults[command][0]} {num2}"), 2)


calculating("adding")
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
you want and adding range, e.g "add 50000 5000000"
If you want this message to reappear, type "cancel".
""")


command = "cancel"
command_stopper = False
while True:
    if command == "cancel": #pops up help menu
        helping()
        command = input("What would you like to do? ")
    else:
        if command in defaults:
            result = calculating(command)  #prints equation, and saves its result to result
            yourResult = float(input("Enter your result: "))
            while yourResult not in (result, "cancel"):
                yourResult = float(input("Enter your result: "))
