import polars as pl


def main():
    df = pl.DataFrame({"id": [1, 2, 3], "value": [10, 20, 30]})
    mean_value = df.select(pl.col("value").mean()).item()
    print(f"The mean value is: {mean_value}")


if __name__ == "__main__":
    main()
