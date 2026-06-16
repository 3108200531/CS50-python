import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # re.IGNORECASE handles variations like <IFRAME SRC=...>
    # [^">] ensures we don't bleed into other HTML attributes
    match = re.search(
        r'<iframe[^>]*\bsrc="https?://(?:www\.)?youtube\.com/embed/([^"]+)"',
        s,
        re.IGNORECASE,
    )

    if match:
        # Extract the exact video ID group
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    return None


if __name__ == "__main__":
    main()
