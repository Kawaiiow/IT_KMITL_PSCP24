# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    distribute.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 13:45:36 by kawaii            #+#    #+#              #
#    Updated: 2024/10/05 00:37:24 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Sharing is caring"""

def main():
    """void"""
    money = int(input())
    n = int(input())
    if money < n or (n == 1 and money != 8):
        print("-1")
        return
    if money == n * 8:
        print(n)
    elif money > n * 8:
        print(n - 1)
    else:
        money -= n
        np = money // 7
        if money % 7 == 3 and n - (money // 7) == 1:
            np -= 1
        print(np)
main()
