# An array is monotonic if it is either monotone increasing or monotone decreasing. an array is monotone
# increasing if all its elements from left to right are non-decreadsing. An array is monotone decreasing 
# if all itss elemtss from left to right are non-increasing. given an integer array return true if the 
#  the given array is monotonic or false otherwise

def monotonic_arr(arr):

    if arr[0] > arr[len(arr)-1 ]:
        for i in range(len(arr) -1 ):
            if arr[i] < arr[i+1]:
                return False
            
    elif arr[0] < arr[len(arr)-1]:
        for i in range(len(arr) -1 ):
            if arr[i] > arr[i+1]:
                return False
            
    else : 
        for i in range(len(arr) -1 ):
            if arr[i] != arr[i+1]:
                return False
            
    return True

# arr = [1,2,3,4,5]
# arr = [ 5,4,3,2,1]
arr = [1,2,3,2,1]

print(monotonic_arr(arr))
