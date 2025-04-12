#!/usr/bin/env python3

def main():
    num = float(input())
    if num == 0:
        print("This number is both positive and negative.")
    elif num > 0:
        print("This number is positive.")
    elif num < 0:
        print("This number is negative.")

main()