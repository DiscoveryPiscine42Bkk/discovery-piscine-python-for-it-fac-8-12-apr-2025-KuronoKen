#!/usr/bin/env python3

def main():
    password = "12345"
    incoming = input()
    if password == incoming:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
main()