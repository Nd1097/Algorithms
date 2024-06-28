# Bubble sort is a special type of sorting algorithm which has boundations on the input range but if the constraints staisfies then it can sort the array in linear time with o(n).

# Pseudo code 
# def bubble(arr, counts):
#     for n in arr:

#         counts[n]+=1

#     i=0
#     for n in range(0,len(counts)):
#         for j in range(0,counts[n]):
#             arr[i] = n
#             i+=1

#     return arr

arr = [2,1,2,0,0,2]
counts = [0,0,0]

def bubble(arr, counts):

    for n in arr:
        counts[n]+=1

    i=0

    for n in range(len(counts)):
        for j in range(0,counts[n]):
            arr[i] = n
            i+=1
    return arr

print(bubble(arr, counts))


