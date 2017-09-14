
#!/usr/bin/python

# insert rank calculate

def insert_sort(list):
    count = len(list)
    for i in range(1 , count):
        key = list[i]
        j = i - 1
        while j >= 0 :
            if list[j] > key :
                list[j + 1] = list[j]
                list[j] = key
            j -= 1

    return list

list = [1 , 5 , 7 , 9 , 2 , 8 , 4]
print insert_sort(list)





