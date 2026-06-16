import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        continue


number = random.randint(1, level)


while True:
    try:
        ask = int(input("Guess: "))
        if ask <= 0:
            continue
    except ValueError:
        ask = int(input("Guess: "))

    if ask == number:
        print("Just right!")
        break
    elif ask < number:
        print("Too small!")
        continue
    else:
        print("Too large!")
        continue
