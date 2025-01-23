import numpy as np
from PIL import Image
from load_image import ft_load


def ft_zoom(path: str, x: int, y: int) -> np.array:
    ft_load(path)
    img = Image.open(path).convert("L")
    width, height = img.size
    print(width, " | ", height)
    new_width = int(width * x)
    new_height = int(height * y)
    print(new_width, " | ", new_height)
    new_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    new_img.save("test.jpg")
    return


def main():
    ft_zoom("animal.jpeg", 10, 10)
    return


if __name__ == "__main__":
    main()
