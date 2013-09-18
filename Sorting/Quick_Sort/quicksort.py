import math
import os

def partition(array,left,right,pivotindex):
    pivot = array[pivotindex]
    # print("\n {pivot}").format(pivot=pivot)
    # print("\n Array before {0}").format(array)
    array[right],array[pivotindex] = array[pivotindex],array[right]
    # print("\n Array after {0}").format(array)

    storeindex=left
    
    for i in xrange(left,right):
        if(array[i]<array[right]):
            array[i],array[storeindex] = array[storeindex],array[i]
            storeindex = storeindex + 1
    array[storeindex],array[right] = array[right],array[storeindex]
    return storeindex

def quicksort(array,left,right):
    if left<right:
        mid = (left+right)/2
        newpivotindex = partition(array,left,right,mid)
        print array
        quicksort(array,left,newpivotindex-1)
        quicksort(array,newpivotindex+1,right)
    return array

def main():
    array = [10,9,8,7,6,5,4,8,3,2]
    print (quicksort(array,0,len(array)-1))

if __name__ == '__main__':
    main()
