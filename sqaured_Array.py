#  method 01
# time complexty O(NlogN)
def square_array(arr):
    
    for i, num in enumerate(arr) :
        arr[i] = num **  2
    arr.sort()
    return arr
    

arr = [ -1,-2,-3, 0, 1, 2, 3]
print(square_array(arr))

#  method 2
#  time complexety O(N)
# def square_array(arr):
#     new_arr = [0]*len(arr)
#     i = 0
#     j = len(arr) -1 

#     for k in reversed(range(len(arr))):
        
#         if arr[j]**2 > arr[i]**2:
#             new_arr[k] = arr[j]**2
#             j -=1
#         else:
#             new_arr[k] = arr[i]**2
#             i +=1
#     print(new_arr)

# square_array([-2, -1, 0, 3,4])
        