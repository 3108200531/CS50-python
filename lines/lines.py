import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    filename = sys.argv[1]
    count = 0

    try:
        with open(filename) as file:
            for line in file:
                line = line.lstrip()

                if line.strip() == "":
                    continue
                if line.startswith("#"):
                    continue

                count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")

    print(count)

if __name__ == "__main__":
    main()
