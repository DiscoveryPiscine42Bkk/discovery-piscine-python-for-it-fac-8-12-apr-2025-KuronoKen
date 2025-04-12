#!/usr/bin/env python3

def main():
    print("Enter a number less than 25")
    num = int(input())
    if num > 25:
        print("Error")
        return
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1
main()