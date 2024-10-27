def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


   
arr = [42, 17, 8, 99, 23, 56, 3, 74]

print("Lista original:", arr)
bubblesort(arr) 
print("Lista ordenada:", arr)
