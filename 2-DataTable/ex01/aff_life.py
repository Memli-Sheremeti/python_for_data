import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(dataset: pd.DataFrame, country: str):
    row = dataset[dataset["country"] == country]
    if row.empty:
        print("Country not found in the database!")
        return
    row = row.drop("country", axis=1).T
    row.plot(title=f'{country} Life Expectancy Projection', figsize=(8, 6),
             legend=False)
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.show()
    return


def main():
    arr = load("life_expectancy_years.csv")
    aff_life(arr, "France")
    aff_life(arr, "1")
    aff_life(arr, "abc")
    aff_life(arr, True)
    return


if __name__ == "__main__":
    main()
