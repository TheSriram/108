import math
def merge(left,right):
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]>right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result+=left[i:]
    result+=right[j:]
    return result

def mergesort(array):
    if len(array)<=1:
        return array
    mid=(len(array))/2
    left=mergesort(array[mid:])
    right=mergesort(array[:mid])
    return merge(left,right)

def main():
    to_be_sorted = mergesort([10,9,8,7,6,5,4,3,2,1])
    print(to_be_sorted) 
if __name__ == '__main__':
    main()
