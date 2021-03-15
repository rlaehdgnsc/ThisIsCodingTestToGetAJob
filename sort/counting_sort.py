array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

cnt_sort = [0]*(max(array)+1)

for i in array:
    cnt_sort[i]+=1

for idx,val in enumerate(cnt_sort):
    for i in range(val):
        print(idx ,end=' ')
    