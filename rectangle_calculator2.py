#!/usr/bin/env python3

# Created by: Ben Lapuhapo
# Created on: September 14 2019
# This program calculates area and perimeter of a rectangle that the user gave


def main():
#   #input
    print("")
    length = int(input("Please enter the rectangle's length: "))
    print("")
    width = int(input("Please enter the rectangle's width: "))
#   #process
    area = length*width
    perimeter = 2*(length+width)
#   #output
    print("")
    print("Area is {}mm^2".format(area))
    print("Perimeter is {}mm".format(perimeter))

if __name__ == "__main__":
    main()
