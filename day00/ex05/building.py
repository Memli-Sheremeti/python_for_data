# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    building.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/24 11:43:26 by mshereme          #+#    #+#              #
#    Updated: 2024/12/24 12:40:38 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
    symbol_dic = {"lower" : 0, "upper" : 0, "space" : 0, "digit" : 0, "symbol" : 0}
    try:
        assert len(sys.argv)  == 2
    except AssertionError:
      print('AssertionError: more than one argument is provided')
      return
    
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
    
    print("The text contains", sum(symbol_dic.values()) - symbol_dic["space"], "characters:")
    


if __name__ == "__main__":
    main()