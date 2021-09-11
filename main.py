import random
import string


def main():
    genamount = int(input("Type in the amount of codes to generate: "))
    iterate = 1
    while genamount >= iterate:
        code = "https://discord.gift/" + (''.join(random.choices(string.digits + string.ascii_letters, k=random.randrange(17, 20))))
        txt = open("codes.txt", "a+")
        txt.write(f"{code}\n")
        txt.close()
        print(f"[GEN] - {code}")
        iterate += 1


if __name__ == "__main__":
    main()
