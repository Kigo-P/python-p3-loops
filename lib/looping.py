#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    numbers = 10
    while numbers >=0:
        if numbers > 0:
            print(numbers)
        else:
            print("Happy New Year!")
        numbers -=1

happy_new_year()
def square_integers(int_list):
    # code goes here!
    integer_list = [integers**2 for integers in int_list ]
    return integer_list
    # for integers in int_list:
    #     print(integers**2)

square_integers([1,2,3,4,5])

def fizzbuzz():
    # code goes here!
    for numbers in range(1, 101, 1):
        #print(numbers)
        if numbers%3 == 0 and numbers%5 == 0:
            print("FizzBuzz")
        elif numbers%3 == 0:
            print("Fizz")
        elif numbers%5 == 0:
            print("Buzz")
        else:
            print(numbers)

fizzbuzz()