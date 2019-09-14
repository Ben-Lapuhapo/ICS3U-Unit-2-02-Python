#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 14 2019
# This program calculates area and perimeter of a rectangle that the user gave 


import math


def main():
    print("Rectangle calculator")
    print("")
    length = int(input("Please enter the rectangle's length: "))
    print("")
    width = int(input("Please enter the rectangle's width: "))
    print("")
    print("The rectangle's  given dimensions are:")
    print("Length: ",length,".cm")
    print("Width: ",width,".cm")
    print("The rectangle's perimeter is {}".format(2*length+2*width))
    print("The rectangle's area is {}".format(length*width))

if __name__ == "__main__":
    main()