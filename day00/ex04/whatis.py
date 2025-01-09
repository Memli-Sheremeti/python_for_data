# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 23:04:15 by mshereme          #+#    #+#              #
#    Updated: 2025/01/09 19:25:18 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def oven_or_odd(object: any):

    assert len(object) == 2, "AssertionError: more than one argument is provided"
    
    try :
        int(object[1])
    except ValueError:
        raise AssertionError("AssertionError: argument is not an integer")

    if int(object[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main() :
    try :
        oven_or_odd(sys.argv)
    except AssertionError as e:
        print(e)

if __name__ == "__main__" :
    main()