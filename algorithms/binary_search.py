
my_list = [0, 1, 2, 5, 4, 5, 6, 42]

def binary_search(l, target):
    left = 0
    right = len(l) - 1
    while left <= right:
        middle = (right + left)//2
        if target == l[middle]:
            return middle
        elif target < l[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1



print(binary_search(my_list, 42))
