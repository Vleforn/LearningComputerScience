# quick sort algorithm with recursion
from typing import List


# 4 1 2

def qsort(l: List[int]) -> List[int]:
    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i<=pivot]
        greater = [i for i in l[1:]if i>=pivot]
        return qsort(less) + [pivot] + qsort(greater)
 

assert qsort([]) == []
assert qsort([1]) == [1]
assert qsort([3, 2]) == [2, 3]
assert qsort([1, 56, 2, 15, 7]) == [1, 2, 7, 15, 56]