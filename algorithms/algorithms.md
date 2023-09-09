## Binary search

```python
def binary_search(l: list, target):
  left = 0
  right = len(l)
  
  while l <= r:
    middle = floor((right - left)/2)
    if target == l[middle]:
      return middle
    elif target < l[middle]:
      r = middle
    else:
      l = middle
      
```

