import json

from libs import divide
from modules.multiply import multiply


def main():
    multiply_result = multiply(4, 5)
    print(f"The product of 4 and 5 is: {multiply_result}")

    division_result = divide.divide(20, 4)
    print(f"The division of 20 by 4 is: {division_result}")

    with open("config/config.json", "r") as file:
        config = json.load(file)
        print(f"Config loaded: {config}")


if __name__ == "__main__":
    main()
