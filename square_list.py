# Author: Samuel Bennett
# Date: 5/12/2021
# Description: Function named square_list takes a list of numbers creates square of the values.


def square_list(oldmanjankins):
    for i in range(len(oldmanjankins)):
        oldmanjankins[i] = oldmanjankins[i] * oldmanjankins[i]


nums = [7, -3, 12, 9]
square_list(nums)
print(nums)
