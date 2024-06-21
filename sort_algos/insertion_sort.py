# Insertion Sort is a stable sorting algorithm with o(n*n) time complexity.

# Pseudo code 
# def insertion_sort(arr):
    # for i in range(1, len(n)):
    #     j = i-1
    #     while (j>=0 and arr[j+1] < arr[j]):
    #         tmp = arr[j+1]
    #         arr[j+1] = arr[j]
    #         arr[j] = tmp
    #         j-=1


arr = [2,3,4,1,6]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i-1

        while j >= 0 and arr[j+1] < arr[j]:
            tmp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = tmp
            j-=1
    return arr 

print(insertion_sort(arr))