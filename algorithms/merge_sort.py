#====================== MERGE
#======================== SORT
#========================== ALGORITHM
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

def mergeSort(arr,min,max):
    if(min>=max):
        return
    # here we tell python that we want only the result in Integer
    middle = (max+min)//2
    #left array
    mergeSort(arr,min,middle)
    #right array
    mergeSort(arr,middle+1,max)
    #after we merge
    merge(arr, min,max,middle)

def merge(arr,min,max,middle):
    # we make a copy of the two arrays
    left_array = arr[min:middle+1]
    right_array = arr[middle+1:max+1]

    #we initialize the index
    left_index=0
    right_index=0

    # the sorted array started at the min always
    sorted_array_index = min

    #we compare the values of the two sub arrays
    while(left_index<len(left_array) and right_index<len(right_array)):
        # we compare the values
        if(left_array[left_index]<=right_array[right_index]):
            arr[sorted_array_index]=left_array[left_index]
            left_index+=1
        # we do the opposite of the previous condition
        else:
            arr[sorted_array_index] = right_array[right_index]
            right_index += 1

        #we increment finally the index of the sorted array
        sorted_array_index+=1

    # finally we take the remaining values in the two subarrays(left array par)
    while(left_index<len(left_array)):
        arr[sorted_array_index]=left_array[left_index]
        left_index+=1
        sorted_array_index+=1

    # same (right array part )
    while(right_index<len(right_array)):
        arr[sorted_array_index]=right_array[right_index]
        right_index+=1
        sorted_array_index+=1

print("========================== UNSORTED ARRAY =========================")
initializeAnArray(default_number,array)
displayTheArray(array)
print("=========================== SORTED ARRAY =================================")
mergeSort(array,0,len(array)-1)
displayTheArray(array)