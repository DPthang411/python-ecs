def linear_search(arr,target):
    for i in  arr:
        if i == target:
            print(arr.index(i))
arr = [1,2,3,5,7,43,65]
tar = 3
linear_search(arr, tar)