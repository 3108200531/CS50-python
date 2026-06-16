import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Match exactly four groups of digits separated by periods
    # ^ and $ ensure the entire string must match, preventing partial matches
    match = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip.strip())

    if not match:
        return False

    # Extract the four matched groups
    groups = match.groups()

    for part in groups:
        # Check for invalid leading zeros (e.g., "01" or "001"), but "0" by itself is valid
        if len(part) > 1 and part.startswith("0"):
            return False

        # Check if the numeric value is within the valid 0-255 range
        if not (0 <= int(part) <= 255):
            return False

    return True


if __name__ == "__main__":
    main()
