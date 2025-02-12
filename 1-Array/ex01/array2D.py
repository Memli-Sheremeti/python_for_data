import numpy as np


def parsing_list(family: list):
    """ PARSE IF THE INUPT IS A LIST"""
    if type(family) is not list:
        raise ValueError("Not a list")
    return


def slice_me(family: list, start: int, end: int) -> list:
    """Parameters 2D array: list - an start: int and a end: int.
    Slicing method use for returning a truncated version"""
    try:
        parsing_list(family)
        family_slice = np.array(family)
        print("My shape is :", family_slice.shape)
        print("My name shape is :", family_slice[start:end].shape)
        return family_slice[start:end].tolist()
    except ValueError as e:
        print(f"ValueError: {e}")
        return


def main():
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    slice_me(family, 0, 2)
    slice_me(family, 1, -2)
    print(slice_me(family, 0, 4))
    return


if __name__ == "__main__":
    main()
