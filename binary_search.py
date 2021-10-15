# Author:   Drew D. Lenhart
#
# Desc:     Iterative searching through a sorted array.
#
# Date:     Oct 15 2021
#
#

def binary_search(array, search) -> int:
    start, end, count = 0, len(array), 0

    while (start <= end):
        count+=1
        middle = (start + end) // 2

        try:
            search == array[middle]
        except IndexError:
            return None

        if search == array[middle]:
            return middle
        elif search < array[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return None


arr = [2, 3, 4, 5, 6, 10, 15, 16, 23, 55]
search = 10

print(binary_search(arr, search))