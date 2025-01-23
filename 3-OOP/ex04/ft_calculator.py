class calculator:
    """Cacluator class."""
    def __init__(self, vector: list):
        self.vector = vector.copy()
        super().__init__()

    def __add__(self, object) -> None:
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        if object == 0:
            raise ZeroDivisionError
        self.vector = [x / object for x in self.vector]
        print(self.vector)

    def _decoracor(foo):
        def wrapper(V1, V2, *args, **kwargs):
            print(f"{foo.__name__} is : ", end="")
            foo(V1, V2, *args, **kwargs)
        return wrapper

    @_decoracor
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        V3 = [a * b for a, b in zip(V1, V2)]
        print(sum(V3))
        return

    @_decoracor
    def add_vec(V1: list[float], V2: list[float]) -> None:
        V3 = [a + b for a, b in zip(V1, V2)]
        print(V3)
        return

    @_decoracor
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        V3 = [a - b for a, b in zip(V1, V2)]
        print(V3)
        return


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)


if __name__ == "__main__":
    main()
