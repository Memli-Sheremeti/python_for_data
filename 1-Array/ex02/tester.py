from load_image import ft_load


def main():
    print(ft_load(None))
    print("-----------------------------")
    print(ft_load("not_a_file.jpg"))
    print("-----------------------------")
    print(ft_load("landscape.jpg"))
    print("-----------------------------")
    print(ft_load("animal.jpeg"))


if __name__ == "__main__":
    main()
