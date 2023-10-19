arr = [1, 2, 3, 4, 5]

def calculate_prefix_sum(arr):
    prefix_sum = [0] * len(arr)
    prefix_sum[0] = arr[0]

    for i in range(1, len(arr)):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    
    return prefix_sum

print(arr)
print(calculate_prefix_sum(arr))

# ToDo
# range Sum