def arraySort012(arr):
    N = len(arr)
    ze = 0
    one = 0
    two = N-1
    while one <=two:
        if arr[one]==0:
            arr[ze],arr[one]=arr[one],arr[ze]
            ze+=1
            one+=1
        elif arr[one]==1:
            one+=1
        elif arr[one]==2:
            arr[one],arr[two]=arr[two],arr[one]
            two -=1
    return arr
