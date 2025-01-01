def largest_num(arr):
    max = 0
    for i in arr:
        if i > max:
            max = i
        else:
            continue
    return max
def second_largest(arr):
    largest = largest_num(arr)
    sec_largest = 0
    for i in arr:
        if i < largest and i > sec_largest:
            sec_largest = i
        else:
            continue
    return sec_largest
arr = [1,2,3]
print(second_largest(arr))