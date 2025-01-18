import numpy as np
from load_image import ft_load
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:
    try:
        invert = 255 - array
    except Exception:
        print("Exception: error ft_invert")
        exit(1)
    return invert


def ft_red(array) -> np.array:
    try:
        red_arr = np.array(array)
        red_arr[:, :, 1] = 0
        red_arr[:, :, 2] = 0
    except Exception:
        print("Exception: error ft_red")
        exit(1)
    return red_arr


def ft_green(array) -> np.array:
    try:
        green_arr = np.array(array)
        green_arr[:, :, 0] = 0
        green_arr[:, :, 2] = 0
    except Exception:
        print("Exception: error ft_green")
        exit(1)
    return green_arr


def ft_blue(array) -> np.array:
    try:
        blue_arr = np.array(array)
        blue_arr[:, :, 0] = 0
        blue_arr[:, :, 1] = 0
    except Exception:
        print("Exception: error ft_blue")
        exit(1)
    return blue_arr


def ft_grey(array) -> np.array:
    try:
        gray_arr = np.array(array)
        gray_arr = gray_arr.mean(axis=2, keepdims=True).astype(np.uint8)
        print(gray_arr)
        np.repeat(gray_arr, 3, axis=2)
    except Exception:
        print("Exception: error ft_grey")
        exit(1)
    return gray_arr


def main():
    img = ft_load("landscape.jpg")
    print(img)
    img = ft_invert(img)
    # ft_red(img)
    # ft_green(img)
    # ft_blue(img)
    # ft_grey(img)
    # ft_invert((1, 2, 3))
    # ft_red([])
    # ft_green(12)
    # ft_blue(True)
    # ft_grey([[1, 2, 3]])
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap="gray")
    plt.show()
    return


if __name__ == "__main__":
    main()
