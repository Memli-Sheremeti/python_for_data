# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/24 11:43:26 by mshereme          #+#    #+#              #
#    Updated: 2025/01/09 20:13:36 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import string

def prompte_user():
    try :
        user_input = input("What is the text to count?\n")
        sys.argv.append(user_input)
    except EOFError:
        sys.argv.append("")
        return 
     
def print_the_ouput(object: any):
    print("The text contains", len(sys.argv[1]), "characters:")
    print(object["upper"], "upper letters")
    print(object["lower"], "lower letters")
    print(object["punctuation"], "punctuation marks")
    print(object["space"], "spaces")
    print(object["digit"], "digits")

def calcul_caracteres(object: any):
     for i in sys.argv[1]:
        if i.islower():
            object["lower"] += 1
        elif i.isupper():
            object["upper"] += 1
        elif i.isdigit():
            object["digit"] += 1
        elif i.isspace():
            object["space"] += 1
        elif i in string.punctuation :
            object["punctuation"] += 1
        else :
            continue 

def main():
    symbol_dic = {"lower" : 0, "upper" : 0, "space" : 0, "digit" : 0, "punctuation" : 0}
    
    try:
        assert len(sys.argv)  < 3, "more than one argument is provided"
    except AssertionError as e:
      print(f"AssertionError: {e}")
      return

    if len(sys.argv) == 1:
       prompte_user()

    calcul_caracteres(symbol_dic)
    print_the_ouput(symbol_dic)

if __name__ == "__main__":
    main()
