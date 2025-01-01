def largest_num(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
        else:
            continue
    return max
arr = [2,3,3,2,1,34,34,342,342]
print(largest_num(arr))