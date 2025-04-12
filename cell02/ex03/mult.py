#!/usr/bin/env python3

def isneg(num):
    if num == 0:
        print("The result is both positive and negative.")
    elif num > 0:
        print("The result is positive.")
    elif num < 0:
        print("The result is negative.")

def main():
    print("Enter the first number:")
    num1 = int(input())
    print("Enter the second number:")
    num2 = int(input())
    result = num1*num2
    print(f"{num1} x {num2} = {result}")
    isneg(result)

main()