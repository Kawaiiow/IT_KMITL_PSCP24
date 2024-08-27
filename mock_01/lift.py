# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    lift.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 13:05:20 by kawaii            #+#    #+#              #
#    Updated: 2024/08/26 13:17:30 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Elevator Escalator"""

def main():
    """void"""
    n = int(input())
    limit = float(input())
    total_w = 0
    safe_state = 1
    age_state = 0

    if not n:
        print("Safe")
        return
    for _ in range(n):
        age = int(input())
        w = float(input())
        total_w += w
        if age >= 12:
            age_state = 1
        if total_w > limit:
            safe_state = 0
    if safe_state and age_state:
        print("Safe")
    else:
        print("Not Safe")
main()
