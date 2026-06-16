def convert(text):
    return text.replace(" ", "").replace("-","")


def main():
    answer = convert(input("What is the answer to the Great Question of Life, the Universe and Everything?").lower())


    match answer:
        case "42" | "fortytwo":
            print("Yes")
        case _:
            print("No")


main()
