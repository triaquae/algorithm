#_*_coding:utf-8_*_
__author__ = 'Alex Li'



#source = [10,3,93,21,44,5,4,9,11]
source = [6, 8, 43, 55, 67, 67, 77, 84, 85, 92]


count = 0
for i in range(len(source)):
    for j in range(i,len(source)):
        source_ele = source[i] #要被拿来对比且替换的原始值

        if source[j] < source_ele : #只要这个列表后面的值比最前面的值大,那就把它俩个做个对调
            source[i] = source[j]
            source[j] = source_ele
        count +=1
    print(source)
print("运行次数:",count)
