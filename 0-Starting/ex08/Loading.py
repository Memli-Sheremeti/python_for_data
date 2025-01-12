import sys
from time import sleep
from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    print(type(lst))
    print(lst)
    sys.stdout.write(f"\rProgress: {1}/{max(lst) + 1}")
    sys.stdout.flush()
    print(iter(lst))
    sleep(0.05)
    return 


def main():
    for elem in ft_tqdm(range(100)):
        sleep
    return


if __name__ == "__main__":
    main()
