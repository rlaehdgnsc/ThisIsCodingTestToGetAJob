array = [7,5,9,0,3,1,6,2,4,8]

print("before sort: ",array)
for i in range(len(array)-1):
    m = i
    for j in range(i+1,len(array)):
        if array[m]>array[j]:
            m = j
    array[m], array[i] = array[i], array[m]

print("after sort: ", array)
    