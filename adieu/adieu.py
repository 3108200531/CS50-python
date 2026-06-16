import inflect

def main():
    p = inflect.engine()
    names = []

    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print()
            break

    output = p.join(names)

    print(f"Adieu, adieu, to {output}")

if __name__ == "__main__":
    main()
