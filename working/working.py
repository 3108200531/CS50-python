import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Regex Breakdown:
    # (\d\d?)(?::(\d\d))? (AM|PM) -> Matches hours, optional minutes, and AM/PM
    # There must be a strict " to " in between the two times
    pattern = r"^(\d\d?)(?::(\d\d))?\s(AM|PM)\sto\s(\d\d?)(?::(\d\d))?\s(AM|PM)$"
    match = re.search(pattern, s.strip())

    if not match:
        raise ValueError("Invalid format")

    # Extract all 6 captured pieces
    shour, smin, speriod, ehour, emin, eperiod = match.groups()

    # Convert minutes (default to "00" if not provided in input)
    smin = smin if smin else "00"
    emin = emin if emin else "00"

    # Validate numbers and parse to 24-hour strings
    start_time = parse_time(shour, smin, speriod)
    end_time = parse_time(ehour, emin, eperiod)

    return f"{start_time} to {end_time}"


def parse_time(hour_str, min_str, period):
    hour = int(hour_str)
    minute = int(min_str)

    # Validate logical range boundaries
    if hour < 1 or hour > 12 or minute < 0 or minute >= 60:
        raise ValueError("Time values out of range")

    # 12-hour to 24-hour conversion logic
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12

    # Format integers with leading zeros to match 24-hour format (e.g., "09:00")
    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
