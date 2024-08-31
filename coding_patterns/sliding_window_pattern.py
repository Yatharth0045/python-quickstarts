# Sliding Window pattern

## Usecase: Find max sum in a k window in an array

arr = [3,2,7,5,9,6,2,6,8,9,9,9,2,3]
k = 5

def get_max(arr,k):
    max = sum(arr[:k])
    total = max
    sub_arr = arr[:k]
    print(total)
    for i in range(1, len(arr)-k+1):
        total = max - arr[i-1] + arr[k+i-1]
        print(total)
        if total > max:
            max = total
            sub_arr = arr[i:k+i]
    
    return max,sub_arr
    
m, s = get_max(arr,k)
print('max is',m,'with subarray',s)

