import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    file = sys.argv[1]

    with open(file) as file:
        reader = csv.reader(file)
        rows = list(reader)

    print (tabulate(rows[1:], rows[0],tablefmt="grid"))

if __name__ == "__main__":
    main()


