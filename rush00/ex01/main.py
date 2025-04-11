from checkmate import checkmate
import sys

def main():
    boardfiles = sys.argv[1:]
    if not boardfiles:
        print("There is no file in the arguments.")
    for file in boardfiles:
        with open(file, 'r') as f:
            board = f.read()
            checkmate(board)

if __name__ == "__main__":
    main()