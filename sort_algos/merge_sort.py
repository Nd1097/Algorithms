# Merge sort is a Divide and Conquer stable Algorithm, it has a time complexity of o(nlogn). is is usually preferred over insertion sort.

# Pseudo code 

# def mergeSort(arr, s, e): s and e are pointers 

#     if (e-s+1 <= 1): base case 
#         return arr
    
#     m = (e+s)/2

#     mergeSort(arr, s, m)  2 branch recursion step
#     mergeSort(arr, m+1, e)

#     merge(arr s, e, m)  merging step, uses 2 pointer technique

#     return arr

arr = [2,3,4,1,6]

def merge(arr, s, e , m):
    # copy both the sorted arrays into tmp arrays
    L = arr[s : m+1]
    R = arr[m+1 : e+1]

    # pointer for all the arrays:
    i = 0
    j = 0
    k = s

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1

    while i < len(L):
        arr[k] = L[i]
        i+=1
        k+=1
    
    while j < len(R):
        arr[k] = R[j]
        j+=1
        k+=1


def mergeSort(arr, s, e):

    if e-s+1 <=1 :
        return arr
    
    m = (e+s)//2

    mergeSort(arr, s, m)
    mergeSort(arr, m+1, e)

    merge(arr, s, e, m)

    return arr


print(mergeSort(arr, 0, len(arr)))