# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    niwarn_world.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kawaii <kawaii@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/08/26 13:19:21 by kawaii            #+#    #+#              #
#    Updated: 2024/08/26 13:28:16 by kawaii           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

"""Parallel World"""
import math

def sins(n):
    """float"""
    return math.sin(math.radians(n))

def x_cal(n):
    """float"""
    return 2 + ((math.log2(n ** 2)) / ((2 * n) * math.log2(n)))

def y_cal(s, n):
    """float"""
    return (sins(30) + math.sqrt(2 * s)) / (x_cal(n) + 3)

def main():
    """void"""
    n = float(input())
    s = float(input())
    k = float(input())

    x_pos = x_cal(n)
    y_pos = y_cal(s, n)
    z_pos = (y_cal(k, k) ** 2) + ((8456 * (x_cal(k) ** 4)) / (24 * k))
    print(f"X: {x_pos:.1f}, Y: {y_pos:.1f}, Z: {z_pos:.1f}")
main()
