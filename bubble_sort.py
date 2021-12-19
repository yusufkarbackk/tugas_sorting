def bubble_sort(arr):
    array_length = len(arr)

    for i in range(array_length):
        for j in range(array_length-i-1):
            print(i)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)

print(arr)