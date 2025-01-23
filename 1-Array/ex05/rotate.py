import numpy as np
from PIL import Image


def rotateMatrix(arr) -> np.array:
    n = len(arr)
    rotate_arr = np.array(arr)
    for i in range(n):
        for j in range(n):
            rotate_arr[n - j - 1][i] = arr[i][j]
    return rotate_arr


def ft_rotate(path: str) -> np.array:
    try:
        img = Image.open(path)
        gray_img = img.convert("L")
        arr = np.array(gray_img)
        new_img = arr[200:600, 400:800]
        new_img = rotateMatrix(new_img)
        new_img = new_img[:, :, np.newaxis]
        print("New shape after slicing:", new_img.shape)
        img.close()
    except Exception:
        print("Exception with the path:", path)
        return
    return new_img


def main():
    print(ft_rotate("animal.jpeg"))
    print(ft_rotate("caca"))
    return


if __name__ == "__main__":
    main()
