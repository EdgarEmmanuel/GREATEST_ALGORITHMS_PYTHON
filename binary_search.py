#======== BINARY
#=========== SEARCH
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

def binarySearch(valueToFind,array,min,max):
    middleIndex = round((min+max)/2)
    if(array[middleIndex]<valueToFind):
        binarySearch(valueToFind,array,middleIndex+1,max)
    if(array[middleIndex]>valueToFind):
        binarySearch(valueToFind,array,min,middleIndex-1)
    if(array[middleIndex]==valueToFind):
        print("find at index " + str(middleIndex))


initializeAnArray(default_number,array)

#remove the duplicate values in the array
new_array =list(set(array))

#the value to find
numberToFind = array[rand.randint(0,(len(new_array)-1))]
displayTheArray(new_array)

print("Value to find => "+str(numberToFind))
binarySearch(numberToFind,new_array,0,(len(new_array)-1))