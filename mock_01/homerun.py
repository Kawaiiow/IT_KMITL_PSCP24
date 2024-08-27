# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    homerun.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 13:00:38 by kawaii            #+#    #+#              #
#    Updated: 2024/08/26 13:04:53 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Baseball is very popular in Japan??"""

def main():
    """void"""
    n = int(input())
    skill = float(input())
    count = 0

    for _ in range(n):
        ran = float(input())
        if skill > ran:
            count += 1
    print(count)
main()
