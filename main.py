#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program formats your address


def addressing(names, apt_num, str_num, str_name, city, province, post_code):

    # output
    if "" in apt_num:
        print("\n{0}".format(names))
        print("{0} {1}".format(str_num, str_name))
        print("{0} {1} {2}".format(city, province, post_code))

    else:
        print("\n{0}".format(names))
        print("{0} {1} {2}".format(apt_num, str_num, str_name))
        print("{0} {1} {2}".format(city, province, post_code))


def main():
    # this function calls other functions as well as
    #   takes input

    # input
    names = input("Please input your full legal name: ")
    print("Please input your apartment number ", end="")
    apt_num = input("(leave blank for none): ")
    str_num = input("Please input your street number: ")
    str_name = input("Please input your street name: ")
    city = input("Please input your city: ")
    province = input("Please input your province: ")
    post_code = input("Please input your postal code: ")

    # call fucntions
    addressing(names, apt_num, str_num, str_name, city, province, post_code)


if __name__ == "__main__":
    main()
