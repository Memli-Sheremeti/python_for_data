from ft_filter import ft_filter


def negatif(x):
    """return true if x < 0"""
    return x < 0


def positif(x):
    """return true if x > 0"""
    return x > 0


def zero(x):
    """return true if x = 0"""
    return x == 0


def main():
    data_set = [-10, -9, -8, 0, 1, 2, 3, 4]
    print(ft_filter(negatif, data_set), " | ", filter(negatif, data_set))
    for x in ft_filter(negatif, data_set):
        print("ft_filter: ", x)
    for x in filter(negatif, data_set):
        print("filter: ", x)
    for x in ft_filter(positif, data_set):
        print("ft_filter: ", x)
    for x in filter(positif, data_set):
        print("filter: ", x)
    for x in ft_filter(None, data_set):
        print("ft_filter: ", x)
    for x in filter(None, data_set):
        print("filter: ", x)


if __name__ == "__main__":
    main()
