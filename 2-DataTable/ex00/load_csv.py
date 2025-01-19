import pandas as pd
import numpy as np


def load(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        print("Loading dataset of dimension ", df.shape)
    except Exception:
        print("Exception: error with ", path)
        return None
    return df


def main():
    print(load("life_expectancy_years.csv"))
    # print(load(True))
    # print(load([1, 2, 3]))
    # print(load(1))
    return


if __name__ == "__main__":
    main()
