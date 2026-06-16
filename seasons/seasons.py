from datetime import date
import inflect
import sys


def main():
    birth_str = input("Date of Birth: ")
    # Calculate the total minutes or exit if input is invalid
    minutes = calculate_minutes(birth_str, date.today())
    # Convert minutes to words and capitalize the sentence
    words = minutes_to_words(minutes)
    print(words)


def calculate_minutes(birth_str, today):
    try:
        # standard ISO format validation (YYYY-MM-DD)
        birth_date = date.fromisoformat(birth_str)
    except ValueError:
        sys.exit("Invalid date")

    # Subtracting dates returns a timedelta object
    delta = today - birth_date
    days = delta.days

    # Ensure we aren't calculating negative time if a future date is passed
    if days < 0:
        sys.exit("Invalid date")

    # Convert total days to minutes
    return days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    # andword="" removes grammatical "and" variations from the string output
    words = p.number_to_words(minutes, andword="")
    # Capitalize the first letter and append " minutes"
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
