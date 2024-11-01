# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ticket_fare.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 13:56:28 by kawaii            #+#    #+#              #
#    Updated: 2024/10/04 01:13:55 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Train??"""

def sauce(start, target):
    """int"""
    if target > start:
        return target, start
    return start, target

def main():
    """void"""
    final = int(input())
    first_stage = int(input())
    f_rate = int(input())
    second_stage = int(input())
    s_rate = int(input())
    t_rate = int(input())
    start = int(input())
    target = int(input())
    total = 0
    ran = 0
    start, target = sauce(start, target)
    if target > final or start < 1:
        print("Error")
        return
    ran = abs(target - start)
    if ran + target > final:
        print("Error")
        return
    if ran > first_stage:
        total += f_rate
    elif ran <= first_stage:
        total += f_rate
    if ran > second_stage + first_stage:
        total += s_rate * (abs(second_stage))
        total += t_rate * (abs(ran - (second_stage + first_stage)))
    elif first_stage < ran <= second_stage + first_stage:
        total += s_rate * (ran - first_stage)
    print(total)
main()
