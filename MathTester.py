from time import time
from random import randint
from sys import stdout, stdin


def printf(text, divider="\n"): #faster print
    text = str(text)
    stdout.write(text + divider)


def input(prompt): #faster input
    stdout.write(prompt)
    return stdin.readline()


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
