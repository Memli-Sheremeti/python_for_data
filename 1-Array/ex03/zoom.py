from load_image import ft_load
import numpy as np
from PIL import Image


def ft_zoom(path: str) -> np.array:
    try:
        object = ft_load(path)
        print(object)
        object = object[200:600, 400:800]
        object = object[:, :, 0]
        print("New shape after slicing:", object.shape)
        print(object)
        return object
    except Exception as e:
        print(f"Exception: {e}")
        return


def main():
    ft_zoom("animal.jpeg")
    return


if __name__ == "__main__":
    main()
