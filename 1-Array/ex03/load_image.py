import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    try:
        image = Image.open(path).convert("RGB")
    except Exception:
        print("Problem with the path:", path)
        return
    arr = np.array(image)
    print("My shape is :", arr.shape)
    image.close()
    return arr


def main():
    ft_load("landscape.jpg")
    ft_load("animal.jpeg")
    ft_load(1)
    ft_load(True)
    ft_load("lol")
    return


if __name__ == "__main__":
    main()
