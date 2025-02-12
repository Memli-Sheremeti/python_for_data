import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """
    Load an image from the given file path and convert it to a NumPy array.

    This function reads an image file, converts it to RGB format,
    and returns it as a NumPy array.
    It uses np.asarray() to ensure minimal overhead when converting the image.

    Args:
        path (str): The file path of the image.

    Returns:
        np.array: A NumPy array representing the image.

    Raises:
        Exception: If the file cannot be opened or processed.
    """
    try:
        # image = Image.open(path).convert("RGB")
        image = Image.open(path)
        arr = np.asarray(image)
        print("My shape is :", arr.shape)
        return arr
    except Exception as e:
        print(f"Exception: {e}")
        return


def main():
    ft_load("landscape.jpg")
    ft_load("animal.jpeg")
    ft_load(1)
    ft_load(True)
    ft_load("lol")
    return


if __name__ == "__main__":
    main()
