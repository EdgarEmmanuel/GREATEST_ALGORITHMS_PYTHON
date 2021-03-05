# ===============INSERTION
# ===============SORT
# ==============ALGORITHM

import random as m

default_array=list()
length_array=10

def initializeAnArray(n,array):
    for i in range(0,n):
        array.append(m.randint(1,n+1))

def displayTheArray(n,array):
    for i in range (0,n):
        print(array[i])

def insertionSort(n,array):
    for i in range(n):
        for j in range(i):
            if(array[j]<array[i]):
                memory=array[i]
                array[i]=array[j]
                array[j]=memory

print("=========unsorted array=============")
initializeAnArray(length_array,default_array)
displayTheArray(length_array,default_array)

print("========== sorted array ===========")
insertionSort(length_array,default_array)
displayTheArray(length_array,default_array)