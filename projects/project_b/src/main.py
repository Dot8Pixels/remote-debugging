from mods.power import power


def main():
    base = 2
    exponent = 3
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is {result}")


if __name__ == "__main__":
    main()
