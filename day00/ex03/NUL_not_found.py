# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NUL_not_found.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 23:01:43 by mshereme          #+#    #+#              #
#    Updated: 2024/12/23 23:01:45 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# from NULL_not_found import NULL_not_found

def NULL_not_found(object: any = None) -> int:
    for name, value in globals().items():
        # print(name, " | ", value)
        if not name.startswith("__") and value is object:
            print(name,"= ", value, type(object))
            return 0
    if object is None:
        return 1
    print("Type not Found")
    return 1


Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))

# NULL_not_found()