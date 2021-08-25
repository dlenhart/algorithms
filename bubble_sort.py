# Author:   Drew D. Lenhart
#
# Desc:     Sorting algorithm, repeatedly swapping adjacent elements if they
#           are in the wrong order ( repeatedly moves the higher value to the
#           right untill all numbers are in sorted order. )
#
# Date:     Aug 25th 2021
#
#

def bubble_sort(list):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(list) - 1):
            if list[i]  > list[i + 1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]

    return list

sort = [2, 44, 6, 8, 15, 33, 21, 77, 82, 99, 101]
print(bubble_sort(sort))
