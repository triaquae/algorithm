#_*_coding:utf-8_*_
__author__ = 'Alex Li'

#source = [6, 8, 43, 55, 67, 67, 77, 84, 85, 92]
data = [56,10, 77, 67, 8, 6, 84, 55, 85, 43, 67]



def fast_sort(source,end_pos):
    print("\033[41;1m***********\033[0m")
    i = 0 #左边哨兵
    #j = len(source) -1 #右边哨兵
    j = end_pos #右边哨兵
    v = source[0]
    while i !=j : #两边哨兵还没相遇
        print(i,j)
        #先从右边开始找一个小于v的值
        while source[j] > v and i!=j: #只要右边的值 不比参照值 小,就一直找,直到找到
            print("finding:", source[j], j)
            j -=1

        while source[i] < v and i !=j:
            i+=1
        print('found --->', i,j)
        print('found --->', source[i],source[j])
        tmp = source[i]
        source[i] = source[j]
        source[j] = tmp

        #继续缩小范围找
        print('-------', source)
        #break
        if i ==  j and i > 0:
            print("i", source[i],i)
            source[0] = source[i]
            source[i] = v
            print(source)

            #fast_sort(source,j) #left
            #fast_sort(source[i:]) #left
    else:
        #if j > 0 :
        fast_sort(source,j) #left
        print("----j:",j,i)


fast_sort(data,len(data)-1)
print(data)