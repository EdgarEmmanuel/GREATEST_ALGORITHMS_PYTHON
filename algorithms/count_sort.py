#======== COUNT
#=========== SORT
#============= ALGORITHM

import random as rand
array = list()
default_number = rand.randint(1,20)
# default_number = len(array)

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

def countSort(array):
    length = len(array)
    temporaryArray = list()
    min=0
    max=0
    #we find the mi and the max in the array
    for i in range(length):
        if(i==0):
            min=array[i]
            max=array[i]
        elif(array[i]<=min):
            min=array[i]
        elif(array[i]>max):
            max=array[i]

    #we create a temporary array with the min and the max
    for j in range(max+1):
        #we put a value of zero at all the index
        temporaryArray.append(0)

    #we count the number in the true array at report it in the temporary array
    for i in range(length):
        temporaryArray[array[i]]+=1

    #now we sort according to the temporary array
    start=0
    end=0
    for j in range(max+1):
        #we put a value of zero at all the index

        if(j==0):
            start=0

        if(temporaryArray[j]!=0):
            #we incremnet the end by doing the sum of the start+the number at this index
            end = start+temporaryArray[j]
            for k in range(start,end):
                array[k]=j
        #we increment the start by the end
        start=end

print("============== UNSORTED ARRAY ===============")
initializeAnArray(default_number,array)
displayTheArray(array)
print("============ SORTED ARRAY ===================")
countSort(array)
displayTheArray(array)