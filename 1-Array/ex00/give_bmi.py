import numpy as np


def parsing_list(height: list[int | float], weight: list[int | float]) -> bool:
    """
    Validates that height and weight lists contain only numbers (int or float)
    and are of equal length.

    Args:
        height (list[int | float]): List of heights.
        weight (list[int | float]): List of weights.

    Returns:
        bool: True if validation passes.

    Raises:
        If lists contain non-numeric values or have different lengths.
    """
    if (all((type(h) is int or type(h) is float) for h in height) is False or
            all(type(w) is int or type(w) is float for w in weight) is False):
        raise Exception("Not int or float in the list")
    elif len(height) != len(weight):
        raise Exception("Not the same length")
    return True


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Checks if each BMI value exceeds a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): The threshold limit.

    Returns:
        list[bool]: indicating whether each BMI value exceeds the limit.
    """
    return (np.array(bmi) > limit).tolist()


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calculates the BMI for each pair of height and weight.

    Args:
        height (list[int | float]): List of heights
        weight (list[int | float]): List of weights

    Returns:
        A list of BMI values corresponding to the input heights and weights.

    Raises:
        Exception: If the height and weight lists fail validation.
    """
    try:
        parsing_list(height, weight)
    except Exception as e:
        print("Exception: ", e)
        return
    array_height = np.square(np.array(height))
    bmi = np.array(weight) / array_height
    return bmi.tolist()


def main():
    test = give_bmi([1, 2, 3], [2, 4, 5])
    print(test)
    return


if __name__ == "__main__":
    main()
