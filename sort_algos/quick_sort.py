# Quick Sort is an Inplace Sorting algorithm with worst case time complexity of 0(n*n) and avaerage case of o(nlogn), it is not a stable sorting algorithm. 

# Pseudo code

# def quickSort(arr, s , e):

#     if (e - s +1 <= 1): Base case scenario
#         return arr
    
#     pivot = arr[e]
#     left = s

#     # Partition: elements smaller than pivot ovr to left 
     
#     for i in range(s, e):
#         if arr[i] < pivot:
#             tmp = arr[left]
#             arr[left] = arr[i]
#             arr[i] = tmp
#             left += 1

#     arr[e] = arr[left]
#     arr[left] = pivot

#     quickSort(arr, s, left-1)
#     quickSort(arr, left+1, e)

#     return arr


arr = [2,3,4,1,6]

def quickSort(arr, s, e):

    if e-s+1 <= 1:
        return arr
    
    pivot = arr[e]
    left = s

    for i in range(s,e):
        if arr[i] < pivot:
            tmp = arr[left]
            arr[left] = arr[i]
            arr[i] = tmp
            left+=1
    
    arr[e] = arr[left]
    arr[left] = pivot

    quickSort(arr, s, left-1)
    quickSort(arr, left+1, e)

    return arr

print(quickSort(arr, 0, len(arr)-1))