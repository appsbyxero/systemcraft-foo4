import sys

# This passes the first task!
def main():
    with open(sys.argv[2], 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')


if __name__ == '__main__':
    main()
