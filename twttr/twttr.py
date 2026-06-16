def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")



def shorten(text):
    result = ""
    for c in text:
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            result += c
    return result

if __name__ == "__main__":
    main()
