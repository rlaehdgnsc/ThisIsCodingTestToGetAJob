array = [7,5,9,0,3,1,6,2,10,4,8]

print("before sort: ",array)

def quickSort(l,r):
    if l>=r:
        return
    pivot = l
    i,j = l+1, r
    while i<=j:
        while i<=r and array[pivot]>=array[i]:
            i+=1
        while j>l and array[pivot]<=array[j]:
            j-=1
        if i<=j:
            array[i],array[j] = array[j],array[i]
        else:
            array[j],array[pivot] = array[pivot],array[j]
    quickSort(l,j-1)
    quickSort(j+1,r)
    
quickSort(0,len(array)-1)
print("after sort: ", array)