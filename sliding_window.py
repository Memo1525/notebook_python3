"""
Porpouse: Efficiently find the sum or maxomium/minium of a fixed-size subarray as it slides across a larger array (original).
Time: O(n) to preprocess the array and O(1) to compute the sum of the array.
"""
# the key of this technique is to quit the last element and add the following in with that we move the window
def max_sum_subarray(arr,k):
    n = len(arr)
    if n < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k,n):
        window_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)
    return max_sum

def min_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None
    window_sum = sum(arr[:k])
    min_sum = window_sum

    for i in range(k,n):
        window_sum += arr[i] - arr[i-k]
        min_sum = min(min_sum, window_sum)
    return  min_sum
