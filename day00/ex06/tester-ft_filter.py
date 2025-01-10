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
        print(x)


if __name__ == "__main__":
    main()
