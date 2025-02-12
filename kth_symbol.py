
def kth_symbol(n, k):
    if n==1 :
        return 1

    length = 2**n-1
    mid_point = length // 2
    
    if k <= length :
        return kth_symbol(n-1,k)
    else :
        return int( not kth_symbol(n-1,k))

print(kth_symbol(4,7))



