#Binary search
#Iterative

def binarySearch(array, x, left, right):
    while left <= right:
        mid = (left + right)//2
        if x == array[mid]:
            return mid
        elif x > array[mid]: # x is on the right side
            left = mid + 1
        else:
            right = mid - 1
    return -1
# recursive
def recursiveBinarySearch(arr, x, l, r):
    if r >= l:
        mid = (l <= r) //2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            recursiveBinarySearch(arr, x, mid+1, r)
        else:
            recursiveBinarySearch(arr, x, l, mid+1)
    else:
        return -1
