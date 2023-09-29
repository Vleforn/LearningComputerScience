def fact(x):
    # base case
    if x < 2:
        return 1
    else:
        return x * fact(x - 1)
    

print(fact(9))