array = [7,5,9,0,3,1,6,2,4,8]

def merge(l,r):
    i,j = 0,0
    sorted_array = []
    while i<len(l) and j<len(r):
        if l[i] <= r[j]:
            sorted_array.append(l[i])
            i+=1
        else:
            sorted_array.append(r[j])
            j+=1

    while i<len(l):
        sorted_array.append(l[i])
        i+=1
    while j<len(r):
        sorted_array.append(r[j])
        j+=1

    return sorted_array

def mergeSort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        l = arr[:mid]
        r = arr[mid:]

        div_l = mergeSort(l)
        div_r = mergeSort(r)
        return merge(div_l,div_r)

    return arr

print("before sort: ",array)
print("after sort: ", mergeSort(array))
