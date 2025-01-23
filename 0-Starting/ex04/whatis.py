import sys


def oven_or_odd(object: any):
    assert len(object) == 2, "more than one argument is provided"
    try:
        int(object[1])
    except ValueError:
        raise AssertionError("argument is not an integer")
        return
    if int(object[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


def main():
    try:
        oven_or_odd(sys.argv)
    except AssertionError as e:
        print("AssertionError:", e)
        return


if __name__ == "__main__":
    main()
