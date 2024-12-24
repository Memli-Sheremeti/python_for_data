# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/24 11:43:26 by mshereme          #+#    #+#              #
#    Updated: 2024/12/24 15:08:10 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    symbol_dic = {"lower" : 0, "upper" : 0, "space" : 0, "digit" : 0, "symbol" : 0}
    try:
        print(len(sys.argv))
        assert len(sys.argv)  < 3
    except AssertionError:
      print('AssertionError: more than one argument is provided')
      return
    
    if len(sys.argv) == 1:
        sys.argv.append(input("What is the text to count?\n"))

    for i in sys.argv[1]:
        if i.islower():
            symbol_dic["lower"] += 1
        elif i.isupper():
            symbol_dic["upper"] += 1
        elif i.isdigit():
            symbol_dic["digit"] += 1
        elif i.isspace():
            symbol_dic["space"] += 1
        else :
            symbol_dic["symbol"] += 1
    
    print("The text contains", len(sys.argv[1]), "characters:")
    print(symbol_dic["upper"], "upper letters")
    print(symbol_dic["lower"], "lower letters")
    print(symbol_dic["symbol"], "punctuation marks")
    print(symbol_dic["space"], "spaces")
    print(symbol_dic["digit"], "digits")
    


if __name__ == "__main__":
    main()