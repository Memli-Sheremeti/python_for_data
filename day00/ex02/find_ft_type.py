# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 20:56:55 by mshereme          #+#    #+#              #
#    Updated: 2025/01/09 17:53:42 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def all_thing_is_obj(object: any) -> int :
    if object.__class__ == list :
        print("List :", type(object))
    elif object.__class__ == tuple :
        print("Tuple :", type(object))
    elif object.__class__ == set :
        print("Set :", type(object))
    elif object.__class__ == dict :
        print("Dict :", type(object))
    elif object.__class__ == str :
        print(object, "is in the kitchen :", type(object))
    else :
        print("Type not found")
    return 42
