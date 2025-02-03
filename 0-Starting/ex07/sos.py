import sys


def ft_parse(object: any):
    """ Parse and process the input provided by the user. """
    assert len(object) == 2, "the arguments are bad"
    parser = object[1].replace(" ", "")
    assert parser.isalnum(), "the arguments are not only alnum"
    return object[1].upper()


def ft_morse_code_output(message, dict):
    """ Translate the strnig in morse code """
    for i in message[:-1]:
        print(dict[i], end=" ")
    for x in message[-1:]:
        print(dict[x])
    return


def main():
    NESTED_MORS = {
                    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
                    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
                    'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
                    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                    'Z': '--..',
                    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                    '8': '---..', '9': '----.', ' ': "/"}
    try:
        string_to_decode = ft_parse(sys.argv)
    except AssertionError as e:
        print("AssertionError:", e)
        return
    ft_morse_code_output(string_to_decode, NESTED_MORS)
    return


if __name__ == "__main__":
    main()
