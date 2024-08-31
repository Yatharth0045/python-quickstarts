## Prefix sum pattern

## Use Case: Sum of elements in a subaarray

arr = [1,2,3,4,5,6,7,8]
i = 3
j = 7

def prefix_sum_arr(arr,same_arr=True):    
    if same_arr:
        # same array
        for i in range(1,len(arr)):
            arr[i] += arr[i-1]
        return arr
    else:
        # Extra space
        arr2 = []
        sum = 0
        for i in arr:
            sum += i
            arr2.append(sum)
        return arr2
    

def get_sum(arr,i,j):
    if i == 0:
        total = arr[j]
    else:
        total = arr[j]-arr[i-1]
    return total


prefix_arr = prefix_sum_arr(arr,False)

total = get_sum(prefix_arr,i,j)

print(arr, i,j,total)
