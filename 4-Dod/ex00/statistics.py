# import numpy as np

def ft_mean(lst: list, dct: dict, N_lst: int, prt: bool = True) -> None:
    if not lst:
        print("ERROR")
        return
    dct["mean"] = sum(lst) / N_lst
    if prt:
        print("mean: ", dct["mean"])
    return


def ft_median(lst: list, dct: dict, N_lst: int, prt: bool = True) -> None:
    if not lst:
        print("ERROR")
        return
    if N_lst % 2 == 0:
        dct["median"] = (lst[(N_lst // 2) - 1] + lst[N_lst // 2]) / 2
    else:
        dct["median"] = lst[((N_lst + 1) // 2) - 1]
    if prt:
        print("median: ", dct["median"])
    return


def ft_quartiles(lst: list, dct: dict, N_lst: int, prt: bool = True) -> None:
    if not lst:
        print("ERROR")
        return
    dct["quartile"] = [lst[((N_lst + 3) // 4) - 1],
                       lst[((3 * N_lst + 1) // 4) - 1]]
    if prt:
        print("quartile: ", dct["quartile"])
    return


def ft_variance(lst: list, dct: dict, N_lst: int, prt: bool = True) -> None:
    if not lst:
        print("ERROR")
        return
    if dct["mean"] == 0:
        ft_mean(lst, dct, N_lst, False)
    v1 = [(x - dct["mean"]) ** 2 for x in lst]
    dct["var"] = (sum(v1) / N_lst)
    if prt:
        print("var: ", dct["var"])
    # np_dct = np.array(lst)
    # mean = np.mean(np_dct)
    # v2 = np.var(np_dct)
    # print(f"mean for np: {mean} my mean={dct["mean"]}")
    # print(f"var for np: {v2} my var={dct["var"]}")
    return


def ft_std_dev(lst: list, dct: dict, N_lst: int, prt: bool = True) -> None:
    if not lst:
        print("ERROR")
        return
    if dct["mean"] == 0:
        ft_mean(lst, dct, N_lst, False)
    if dct["var"] == 0:
        ft_variance(lst, dct, N_lst, False)
    dct["std"] = dct["var"] ** 0.5
    if prt:
        print("std: ", dct["std"])
    # np_dct = np.array(lst)
    # v2 = np.std(np_dct)
    # print(v2)
    return


def ft_statistics(*args: any, **kwargs: any) -> None:
    if (any(isinstance(x, (int, float)) for x in args)) is False and args:
        print("Not int as args!")
        return
    lst = list(args)
    lst.sort()
    dct = {"mean": 0.00,
           "median": 0.00,
           "quartile": [float],
           "std": 0.00,
           "var": 0.00}
    N_lst: int = len(lst)
    for element in kwargs:
        if kwargs.get(element) == "mean":
            ft_mean(lst, dct, N_lst)
        elif kwargs.get(element) == "median":
            ft_median(lst, dct, N_lst)
        elif kwargs.get(element) == "quartile":
            ft_quartiles(lst, dct, N_lst)
        elif kwargs.get(element) == "std":
            ft_std_dev(lst, dct, N_lst)
        elif kwargs.get(element) == "var":
            ft_variance(lst, dct, N_lst)
        else:
            continue
    return


def main():
    return


if __name__ == "__main__":
    main()
