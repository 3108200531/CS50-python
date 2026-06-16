import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    valid_ext = [".jpg", ".jpeg", ".png"]

    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    if input_ext not in valid_ext:
        sys.exit("Invalid input")
    if output_ext not in valid_ext:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    try:
        with Image.open(input_file) as img:
            shirt = Image.open("shirt.png")

            img = ImageOps.fit(img, shirt.size)

            img.paste(shirt, shirt)

            img.save(output_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
