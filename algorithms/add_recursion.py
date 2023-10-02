from typing import List

def add(array: List[int]) -> int:
    # basic case
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        return array[0] + add(array[1:])

    

assert add([]) == 0
assert add([1]) == 1
assert add([1,2]) == 3
assert add([1, 2, 3, 4]) == sum([1, 2, 3, 4])
print(add([1, 2, 3, 4]))
A = [1]
print(A[1:])