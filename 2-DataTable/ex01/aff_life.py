import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load


def aff_life(dataset: pd.DataFrame):
    contry = object["France"]
    print(contry)
    x = object.plot("France", "2012")
    plt.plot(x)
    plt.title("France Life expentancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy Projections")
    plt.show()
    return


def main():
    arr = load("life_expectancy_years.csv")
    print(arr)
    aff_life(arr)
    return


if __name__ == "__main__":
    main()
