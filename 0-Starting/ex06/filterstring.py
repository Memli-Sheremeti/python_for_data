import sys
from ft_filter import ft_filter


def ft_parse(object: any):
    assert len(object) == 3, "the arguments are bad"
    try:
        int(object[2])
    except ValueError:
        raise AssertionError("the arguments are bad")
    return


def ft_filterstring(object: any):
    str_split = object[1].split()
    return list(ft_filter(lambda a: len(a) >= int(object[2]), str_split))


def main():
    try:
        ft_parse(sys.argv)
    except AssertionError as e:
        print("AssertionError:", e)
        return
    data_list = ft_filterstring(sys.argv)
    print(data_list)


if __name__ == "__main__":
    main()
