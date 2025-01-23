import matplotlib.pyplot as plt
import pandas as pd
from load_csv import load
from matplotlib.ticker import FuncFormatter


def formatter_xaxis(x, pos):
    if x >= 1000:
        return f"{int(x) / 1000}k"
    return f"{int(x)}"


def display_the_graph(df_data: pd.DataFrame):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(df_data["gdp_1900"], df_data["life_1900"], alpha=0.7)
    ax.set_xscale("log")
    lowest_gdp = df_data["gdp_1900"].min()
    ax.set_xlim(lowest_gdp - 50, 10000)
    ax.xaxis.set_major_formatter(FuncFormatter(formatter_xaxis))
    ax.set_xticks([300, 1000, 10000])
    ax.set_xlabel("Gross domestic product")
    ax.set_ylabel("Life Expectancy")
    ax.set_title("1900")
    plt.show()


def projection_life(data_income: pd.DataFrame,
                    data_life: pd.DataFrame):
    data_income = data_income[["country", "1900"]].copy()
    data_income.rename(columns={"1900": "gdp_1900"}, inplace=True)
    data_life = data_life[["country", "1900"]].copy()
    data_life.rename(columns={"1900": "life_1900"}, inplace=True)
    df_merged = pd.merge(data_income, data_life, on="country", how="inner")
    df_merged.index = df_merged.index.astype(int)
    display_the_graph(df_merged)
    return


def main():
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    projection_life(income, life)
    return


if __name__ == "__main__":
    main()
