# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mshereme <mshereme@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/23 20:56:52 by mshereme          #+#    #+#              #
#    Updated: 2025/01/09 19:19:57 by mshereme         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime

def main() :
    x = datetime.datetime.now()
    
    print("Seconds since January 1, 1970:" + f"{x.timestamp():,}" + "or" + f"{x.timestamp():.2e}",
    "in scientific notaion\n" + x.strftime("%b"), x.strftime("%d"), x.strftime("%Y"))    

if __name__ == "__main__" :
    main()