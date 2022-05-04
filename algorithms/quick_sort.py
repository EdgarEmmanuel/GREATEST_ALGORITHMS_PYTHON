#======== QUICK
#=========== SORT
#============= ALGORITHM

import random as rand
array = list()
default_number = rand.randint(1,20)

def initializeAnArray(n,array):
    for i in range(0,n):
        array.append(rand.randint(1,n+1))

def displayTheArray(array):
    value=""
    i=0
    while(i<len(array)):
        value+=" | "+str(array[i])
        i=i+1
    print(value)

def quickSort(arr,min,max):
    if(min>=max):
        return
    end = divide(arr,min,max)
    quickSort(arr,min,end-1)
    quickSort(arr,end+1,max)

def divide(array,min,max):
    # get the pivot
    pivot = array[min]
    pivotPosi = min
    # set the min and the max index
    start = min
    end = max

    # while the start index is less than the end index
    while(start<end):
        # if the value at the min is less or equal to the pivot we increment the index of start
        # and the start index different to the length of the array
        while(array[start]<=pivot and start!=len(array)-1):
            start+=1
        # if the value is greater than the pivot we decrement the index of end
        while(array[end]>pivot):
            end-=1
        # if the start index is less than the end index we swap
        if(start<end):
            changePosition(array,start,array[start],end,array[end])

    # if not so we swap the pivot element with the element at the end index
    changePosition(array,pivotPosi,pivot,end,array[end])
    return end


def changePosition(arr,minPosi,minNumber,endPosi,endNumber):
    arr[minPosi] = endNumber
    arr[endPosi] = minNumber

print("================== UNSORTED ARRAY ===============")
initializeAnArray(default_number,array)
displayTheArray(array)
print("================== SORTED ARRAY ==================")
quickSort(array,0,len(array)-1)
displayTheArray(array)