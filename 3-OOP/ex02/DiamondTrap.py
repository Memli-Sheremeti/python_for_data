from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes: str):
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        self.hairs = hairs

    def get_eyes(self):
        return self.eyes

    def get_hairs(self):
        return self.hairs


def main():
    return


if __name__ == "__main__":
    main()
