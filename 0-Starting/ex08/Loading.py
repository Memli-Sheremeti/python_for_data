import sys
import os
from time import sleep


def ft_bar(count, total, prct) -> str:
    """ Creation of the loading bar """
    bar_l, bar_h = os.get_terminal_size()
    bar_l = int(bar_l * 0.75)
    filled_length = (bar_l * count) // total
    bar = "█" * filled_length + "-" * (bar_l - filled_length)
    return bar


def ft_tqdm(lst: range) -> None:
    """ Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""
    iter_ = iter(lst)
    total = len(lst)
    count = 0
    while True:
        try:
            elem = next(iter_)
            count += 1
            prct = count / total * 100
            bar = ft_bar(count, total, prct)
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
