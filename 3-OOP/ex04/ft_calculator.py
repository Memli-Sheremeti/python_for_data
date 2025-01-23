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

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        return

    def add_vec(V1: list[float], V2: list[float]) -> None:
        return

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        return


def main():
    x = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    x + 5


if __name__ == "__main__":
    main()
