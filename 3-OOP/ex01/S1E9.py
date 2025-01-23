from abc import ABC, abstractclassmethod


class Character(ABC):
    """Abstract base class representing a character with a name and life."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialize a character with a name and alive status.
        Args:
            first_name (str): first name of the character.
            is_alive (bool): alive status of the character.
        """
        self.first_name = first_name
        self.is_alive = is_alive
        super().__init__()

    @abstractclassmethod
    def is_alive(self):
        """Abstract method to check if the character is alive.
        Returns: bool: True if the character is alive, False otherwise."""
        pass

    @abstractclassmethod
    def die(self):
        """Abstract method to mark the character as deceased.
        This method should change the alive status to False."""
        pass


class Stark(Character):
    """Class representing a Stark character with a name and life status."""
    def is_alive(self):
        """
        Check if the Stark character is alive.
        Returns:
            bool: True if the character is alive, False otherwise.
        """
        return self.is_alive

    def die(self):
        """This method sets the alive status to False."""
        self.is_alive = False

    def is_name(self):
        """
        Retrieve the name of the Stark character.
        Returns:
        str: The first name of the character.
        """
        return self.name


def main():
    x = Stark("Memli")
    print(x.first_name)
    print(x.is_alive)
    nienke = Stark("Nienke", False)
    print(nienke.__dict__)
    return


if __name__ == "__main__":
    main()
