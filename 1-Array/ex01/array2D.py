import numpy as np


def parsing_list(family: list):
    if type(family) is not list:
        raise ValueError
    return


def slice_me(family: list, start: int, end: int) -> list:
    try:
        parsing_list(family)
        family_slice = np.array(family)
    except ValueError:
        print("ValueError: Not the same number of elements")
        return
    print("My shape is: ", family_slice.shape)
    print("My name shape is: ", family_slice[start:end].shape)
    return family_slice[start:end].tolist()


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    slice_me(family, 0, 2)
    slice_me(family, 1, -2)
    return


if __name__ == "__main__":
    main()
