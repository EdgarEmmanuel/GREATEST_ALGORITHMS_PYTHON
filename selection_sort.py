#=============== SELECTION SORT ALGORITHM ===================

import random as m

default_array=list()
length_array=10

def initializeAnArray(n,array):
    for i in range(0,n):
        array.append(m.randint(1,n+1))

def displayTheArray(n,array):
    value=""
    i=0
    while(i<n):
        value+=" | "+str(array[i])
        i=i+1
    print(value)

def selectionSort(n,array):
    memory=0
    min=10000000000000000000000000000000000000000000000000000000000000
    pos = 0
    for i in range(n):
        min = 10000000000000000000000000000000000000000000000000000000000000
        #we got from i+1 to n to find the min
        for k in range(i+1,n):
            if(array[k]<min):
                min=array[k]
                pos=k
        if((n-1)!=i):
            # we do the change according to the selection sort algorithm
            if(array[pos]<array[i]):
                memory=array[i]
                array[i]=array[pos]
                array[pos]=memory

print("==========================================UNSORTED ARRAY======================")
initializeAnArray(length_array,default_array)
displayTheArray(length_array,default_array)
print("=========================================== SORTED ARRAY =======================")
selectionSort(length_array,default_array)
displayTheArray(length_array,default_array)
