def alternate(array):
    for index,e in enumerate(array, start=0):
        if index % 2 == 0:
            print(e)
list = [1,2,3,4,5,6,7]
alternate(list)