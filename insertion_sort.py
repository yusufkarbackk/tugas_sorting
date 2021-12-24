def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        min = i-1
        
        while min >= 0 and key < arr[min]:
            arr[min + 1] = arr[min]
            min -= 1
        arr[min+1] = key

arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print(arr)