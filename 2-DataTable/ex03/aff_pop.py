import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FuncFormatter, MaxNLocator


def formatter_yaxis(x, pos):
    if x >= 1000:
        return f"{int(x) / 1000}B"
    elif x >= 0:
        return f"{int(x)}M"
    elif x <= 0.001:
        return f"{int(x) * 1000}k"
    else:
        return f"{int(x) * 1000000}"


def display_the_graph(df: pd.DataFrame, country_compared: list):
    df.plot(title='Population Projections', figsize=(8, 6),
            legend=True, color=["blue", "green", "orange", "red", "black"])
    plt.gca().yaxis.set_major_formatter(FuncFormatter(formatter_yaxis))
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=4))
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=8))
    plt.legend(country_compared, loc="lower right")
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.show()
    return


def to_millions(value):
    if 'M' in value:
        return float(value.replace('M', ''))
    elif 'k' in value:
        return float(value.replace('k', '')) / 1000
    elif 'B' in value:
        return float(value.replace('B', '')) * 1000
    else:
        return float(value) / 1000000


def aff_pop(dataset: pd.DataFrame, country_compared: list):
    try:
        country_compared.sort()
    except Exception:
        print("Error on the value sent !")
        return
    df_raw = dataset[dataset["country"].isin(country_compared)]
    if len(df_raw) != len(country_compared):
        print("Error on countries")
        return
    df_raw = df_raw.drop("country", axis=1).T
    df_raw.columns = [country_compared]
    df_raw = df_raw.map(to_millions)
    df_raw = df_raw.loc[:"2050"]
    df_raw.index = df_raw.index.astype(int)
    display_the_graph(df_raw, country_compared)
    return


def main():
    arr = load("population_total.csv")
    aff_pop(arr, ["France", "Belgium"])
    # aff_pop(arr, 1)
    # aff_pop(arr, [1, 2, 3, 4])
    # aff_pop(arr, [False, False])
    return


if __name__ == "__main__":
    main()
