import sys
from time import sleep


def ft_bar(count, total) -> str:
    bar_length = 50
    filled_length = (bar_length * count) // total
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    return bar


def ft_tqdm(lst: range) -> None:
    iter_ = iter(lst)
    total = len(lst)
    count = 0
    while True:
        try:
            elem = next(iter_)
            count += 1
            prct = count / total * 100
            bar = ft_bar(count, total)
            if elem % 20 == 0 or elem == total - 1:
                sys.stdout.write(f"\r{prct:3>,.0f}%|{bar}| {count}/{total}")
                sys.stdout.flush()
            yield elem
        except StopIteration:
            print("")
            break


def main():
    for elem in ft_tqdm(range(333)):
        sleep(0.04)
    return


if __name__ == "__main__":
    main()
