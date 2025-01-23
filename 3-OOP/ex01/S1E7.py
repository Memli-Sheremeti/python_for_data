from S1E9 import Character


class Baratheon(Character):
    """Representing a Baratheon Family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def is_alive(self):
        """
        Check if the Baratheon character is alive.
        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.is_alive

    def die(self):
        """Mark the Baratheon character as deceased.
        This method sets the alive status to False."""
        self.is_alive = False

    def is_name(self):
        """
        Retrieve the name of the Baratheon character.
        Returns:
        str: The first name of the character.
        """
        return self.name

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing a Lannister Family."""
    def __init__(self, first_name: str, is_alive: bool = True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        return cls(first_name, is_alive)

    def is_alive(self):
        """
        Check if the Lannister character is alive.
        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.is_alive

    def die(self):
        """Mark the Lannister character as deceased.
        This method sets the alive status to False."""
        self.is_alive = False

    def is_name(self):
        """
        Retrieve the name of the Lannister character.
        Returns:
        str: The first name of the character.
        """
        return self.name

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


def main():
    print("---")
    return


if __name__ == "__main__":
    main()
