#_*_coding:utf-8_*_
__author__ = 'Alex Li'

#source = [92, 77, 67, 8, 6, 84, 55, 85, 43, 67]
source = [6, 8, 43, 55, 67, 67, 77, 84, 85, 92]

count = 0

for i in range(len(source)):
    current_val = source[i]
    position = i
    #for k in range(i):
    #    print(position_val,i,k)
    print("i:",i)
    print(source)
    count +=1
    while position > 0  and source[position-1] > current_val:
        print(current_val,source[position-1])
        #if current_val < source[position-1]: #如果当前值大于它左边的值 ,就把它放在左边,同时把左边的值 先存下来
        source[position] = source[position-1]

        source[position-1] = current_val
        current_val = source[position-1]
        print("after:",source)
        position -=1
        count +=1

    print('-----')
    #print(source)

print('count:',count)