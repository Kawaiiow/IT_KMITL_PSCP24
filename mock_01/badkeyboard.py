# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    badkeyboard.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 12:56:33 by kawaii            #+#    #+#              #
#    Updated: 2024/08/26 12:58:48 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Buy new one please"""

def main():
    """void"""
    msg = input()
    res = ""

    for c in msg:
        if c == 'i':
            res += 'o'
        elif c == 'o':
            res += 'i'
        elif c == 'I':
            res += 'O'
        elif c == 'O':
            res += 'I'
        else:
            res += c
    print(res)
main()
