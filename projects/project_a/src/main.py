import json

from modules.multiply import multiply


def main():
    result = multiply(4, 5)
    print(f"The product of 4 and 5 is: {result}")

    with open("config/config.json", "r") as file:
        config = json.load(file)
        print(f"Config loaded: {config}")


if __name__ == "__main__":
    main()
