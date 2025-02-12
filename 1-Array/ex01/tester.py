from array2D import slice_me


def main():
    # TEST a int
    x = 1
    print(slice_me(x, 0, 2))
    print("-------------------------------")
    # TEST A Inhomogenous Shape
    family_with_inhomogenous_shape = [[1.80, 78.4],
                                      [2.15],
                                      [2.10, 98.5],
                                      [1.88, 75.2]]
    print(slice_me(family_with_inhomogenous_shape, 0, 2))
    print("-------------------------------")
    # TEST AN EMPTY LIST
    family_none = []
    print(slice_me(family_none, 0, 2))
    print(slice_me(family_none, 1, -2))
    print("-------------------------------")
    # TESTER OF THE SUBJECT
    family = [[1.80, 78.4],
              [2.15, 102.7],
              [2.10, 98.5],
              [1.88, 75.2]]
    print(slice_me(family, 0, 2))
    print(slice_me(family, 1, -2))


if __name__ == "__main__":
    main()
