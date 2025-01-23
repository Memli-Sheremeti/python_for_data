# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 23:04:15 by mshereme          #+#    #+#              #
#    Updated: 2024/12/23 23:43:43 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def oven_or_odd(object: any):
    try:
        assert len(object) == 2
    except AssertionError:
        print ('AssertionError: more than one argument is provided')
        return
    try:
        int(object[1])
    except ValueError:
        print ('AssertionError: argument is not an integer')
        return
    
    if int(object[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

oven_or_odd(sys.argv)