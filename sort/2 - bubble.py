

#!/usr/bin/python

# bubble sort

def bubble_sort(list):
    count = len(list)
    for i in range(0 , count) :
        for j in range(i+1 , count) :
            if list[i] > list[j]:
                list[j] , list[i] = list[i] , list[j]
    return list

list = [1 , 4 , 5 , 3 , 6 , 8 , 2]
print bubble_sort(list)

