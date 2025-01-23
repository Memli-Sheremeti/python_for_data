import sys
import time


def ft_tqdm(lst: range) -> None:
    print(type(lst))
    print(lst)
    for i in lst:
        sys.stdout.write(f"\rProgress: {i + 1}/{max(lst) + 1}")
        sys.stdout.flush()
        time.sleep(0.05)
    return


def main():
    ft_tqdm(range(100))
    return


if __name__ == "__main__":
    main()
