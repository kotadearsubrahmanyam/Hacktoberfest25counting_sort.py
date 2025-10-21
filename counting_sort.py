def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    for i in arr:
        count[i] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i - 1]
        
    for i in range(len(arr)):  # ❌ Should go backward for stability
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

print(counting_sort([4, 2, 2, 8, 3, 3, 1]))  # Expected [1, 2, 2, 3, 3, 4, 8]
