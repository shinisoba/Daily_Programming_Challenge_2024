#merge two sorted arrays
def Merge2nSort(arr1,arr2):
    ptr1, ptr2 = 0,0
    while ptr2<=len(arr2):
        if arr1[ptr1]<arr2[ptr2]:
            ptr1+=1
        elif arr1[ptr1]>=arr2[ptr2]:
