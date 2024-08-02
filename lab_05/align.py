"""Align"""
import math

def main():
    """void"""
    size = int(input())
    align = input()
    strs = input()

    if align == "left":
        print(strs[:size])
    if align == "center":
        if size >= len(strs):
            print(" "*math.ceil((size - len(strs)) / 2),strs,sep="")
        if size < len(strs):
            print(strs[:size])
    if align == "right":
        if size >= len(strs):
            print(" "*(size - len(strs)),strs,sep="")
        if size < len(strs):
            print(strs[:size])
main()
