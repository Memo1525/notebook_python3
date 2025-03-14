"""
Porpuse: Efficeint computation of ranghe of queries
Use: Given an array, we preprocess it into a prefix sum array where each element at index i stores the sum of elements from the start to i. This allows us to compute the sum of any subarray in constant time
Time Cmplexity: O(n)
"""

def prefixSum(arr):
    prefix_arr = [0] * len(arr)
    prefix_arr[0] = arr[0]
    for i in range(1,len(arr)):
        prefix_arr[i] = prefix_arr[i-1] + arr[i]
    return prefix_arr

def rangeSum(prefix, l, r):
    if l == 0:
        return prefix[r]
    else:
        return prefix[r] - prefix[l-1]
