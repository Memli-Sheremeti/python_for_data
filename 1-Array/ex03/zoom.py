import numpy as np
from PIL import Image


def ft_zoom(path: str) -> np.array:
    try:
        img = Image.open(path)
        gray_img = img.convert("L")
        arr = np.array(gray_img)
        new_img = arr[200:600, 400:800]
        new_img = new_img[:, :, np.newaxis]
        print("New shape after slicing:", new_img.shape)
        img.close()
    except Exception:
        print("Exception with the path:", path)
        return
    return new_img


def main():
    (ft_zoom("animal.jpeg"))
    print(ft_zoom("caca"))
    return


if __name__ == "__main__":
    main()
