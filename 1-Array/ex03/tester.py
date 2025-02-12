from zoom import ft_zoom
import matplotlib.pyplot as plt

def main():
    img = ft_zoom("animal.jpeg")
    print(img)
    plt.figure(figsize=(6, 6))
    plt.imshow(img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
