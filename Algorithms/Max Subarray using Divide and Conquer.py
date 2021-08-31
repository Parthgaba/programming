def cross_sub_array_max_sum(arr, low, mid, high):
    left_sum, right_sum, i, j = -999999999,-999999999,mid,mid+1
    s = 0
    max_left, max_right = i, j
    while (i>=low):
        s = s + arr[i]
        if s> left_sum:
            left_sum = s    
            max_left = i
        i -= 1      
    s = 0  
    while (j<=high):
        s = s + arr[j]
        if s> right_sum:
            right_sum = s
            max_right = j
        j += 1   
    return max_left, max_right, left_sum + right_sum     
    
def max_subarray_sum(arr, low, high):
    if high==low:
        return low, high, arr[low]
    else:
        mid = (high+low) // 2
        left_low, left_high, left_sum = max_subarray_sum(arr, low, mid)
        right_low, right_high, right_sum = max_subarray_sum(arr, mid+1, high)
        cross_low, cross_high, cross_sum = cross_sub_array_max_sum(arr, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > right_low and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    res = max_subarray_sum(arr,0,n-1)
    print(res)