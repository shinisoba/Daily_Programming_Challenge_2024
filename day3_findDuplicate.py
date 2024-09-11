def findDuplicate(arr):
    n = len(arr)
    d = {}
    for i in arr:
        d[i] = arr.count(i)
    for i in d:
        if d[i]>1:
            val = i
            return val
