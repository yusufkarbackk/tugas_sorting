def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr)//2  # 3

        # Dividing the array elements
        L = arr[:mid]  # 13 12 11
        # print(L)
        # into 2 halves
        R = arr[mid:]  # 5 6 7
        # print(R)
        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            # print(f'i = {L[i]}')
            # print(f'j = {R[j]}')

            if L[i] < R[j]:
                #print(f'{L[i]} < {R[j]}')
                arr[k] = L[i]
                print(f'baris 29: {k} = {L[i]}')

                i += 1
            else:
                #print(f'{L[i]} > {R[j]}')
                arr[k] = R[j]
                print(f'baris 35: {k} = {R[j]}')

                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            print(f'baris 42: {k} = {L[i]}')
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            print(f'baris 48: {k} = {R[j]}')

            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]

mergeSort(arr)

print(arr)
