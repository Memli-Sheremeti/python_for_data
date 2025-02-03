import sys
import string


def prompte_user():
    """ ASK User the text to analyse """
    print("What is the text to count?")
    user_input = sys.stdin.readline()
    sys.argv.append(user_input)


def print_the_ouput(object: any):
    """ Print the result the analyse """
    if sys.argv[1] != "" and object["EOF"] == 1 and sys.argv[1][-1] != "\n":
        print()
    print("The text contains", len(sys.argv[1]), "characters:")
    print(object["upper"], "upper letters")
    print(object["lower"], "lower letters")
    print(object["punct"], "punctuation marks")
    print(object["space"], "spaces")
    print(object["digit"], "digits")


def calcul_caracteres(object: any):
    """ Calcul of All Caracteres """
    for i in sys.argv[1]:
        if i.islower():
            object["lower"] += 1
        elif i.isupper():
            object["upper"] += 1
        elif i.isdigit():
            object["digit"] += 1
        elif i.isspace() or i == "\r":
            object["space"] += 1
        elif i in string.punctuation:
            object["punct"] += 1
        else:
            continue


def main():
    symbol_dic = {"lower": 0,
                  "upper": 0,
                  "space": 0,
                  "digit": 0,
                  "punct": 0,
                  "EOF": 0}
    try:
        assert len(sys.argv) < 3, "more than one argument is provided"
    except AssertionError as e:
        print(f'AssertionError: {e}')
        return
    if len(sys.argv) == 1:
        prompte_user()
        symbol_dic["EOF"] += 1
    calcul_caracteres(symbol_dic)
    print_the_ouput(symbol_dic)


if __name__ == "__main__":
    main()
