def main():

    ls = {}

    while True:
        try:
            x = input("").lower().strip()
        except EOFError:
            print()
            break
        else:
            x = x.upper()
            ls[x] = ls.get(x, 0) + 1

    for i in sorted(ls):
        print(ls[i], i)

main()
