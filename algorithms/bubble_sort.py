# Bubble sort
from typing import List

my_list = [1, 3, 5, 8, 9, 21, 0, 4]
my_list2 = [1, 2, 3, 4, 5, 7, 6]

def bubble_sort(l: List[int]) -> List[int]:
    length = len(l)
    counter = 0
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        counter += 1
        if swapped == False:
            break
    return l, counter

print(bubble_sort(my_list2))