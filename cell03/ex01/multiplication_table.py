#!/usr/bin/env python3

def main():
    print("Enter a number")
    num = int(input())
    for i in range(10):
        print(f"{i} x {num} = {i*num}")
main()