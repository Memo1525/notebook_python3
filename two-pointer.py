# Common Applications of the 2 pointer technique

# 1 finding pairs in sorted array
# 2 reversing and array or a subarray
# 3 checking for a palindrome
# 4 finding a middle element
# 5 partitioniing and array

def find_pair_with_sum(arr, target):
    left = 0
    right = len(arr) -1
    while left < right:
        current_sum =  arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return False

# I have a method to reverse and array that is
array = [1,2,3]
r_array = array[::-1]

def reverse_array(arr):
    left = 0
    right = len(arr) -1

    while left < right :
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1
    return arr
# in this case if the number is odd it is not important bc it will be in the middle and no modification is needed as it currently sorted

def merge_sorted_arrays(arr1, arr2):
    merged = []
    i, j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append((arr2[j]))
            j += 1
    # add the remaining elements
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

# Reminder of extended in python
