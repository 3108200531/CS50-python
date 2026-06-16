import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    # validators.email(s) returns True if valid, or a ValidationFailure object if not
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
