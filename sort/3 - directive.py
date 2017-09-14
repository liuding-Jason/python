

#!/usr/bin/python

# directive choose sort

def direct_sort(list):
    count = len(list)
    for i in range(0 , count) :
        min = i
        for j in range(i , count) :
            if list[min] > list[j] :
                min = j
        list[min] , list[i] = list[i] , list[min]
    return list

list = [1 , 5 , 4 , 3 , 8 , 6 , 2]
print direct_sort(list)
