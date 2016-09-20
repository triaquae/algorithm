#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import random
import time

def shift_down(arr,node,arr_len):
    left = node * 2 -1  #如果有右孩子,右孩子 的下标
    right = node * 2 +1 -1  #如果有右孩子,右孩子 的下标

    largest = node-1 #默认认为小二叉堆的节点是最大的
    print('node:%s, child:%s arr_len:%s'%(node,left,arr_len))
    while node > 0 and (left  <= arr_len or right <= arr_len): #
        #print("largest:", largest)
        if  (arr_len +1  and arr[largest] <arr[left]):
            largest = left
            #print("-->left:",arr[largest],arr[left])
        if (right < arr_len and arr[largest] < arr[right]):
            largest = right
            #print("-->riht:",arr[largest],node,right)
            #if arr[right] < arr[left]:
            #    largest =arr[left]
        if largest != node-1: #如果相等,代表自己就是最大的,不用换了就
            print("exchange....", arr[node-1], arr[largest])
            tmp = arr[largest]
            arr[largest] = arr[node-1]
            arr[node-1] = tmp
            node = largest
            left = node*2
            right =node*2 +1

        else:
            break

def heap_sort(array):

    last_node = int(len(array) / 2)  #最后一层的节点下标(在堆里)
    to_index = last_node -1 #减1是因为堆下标是从1开始,而列表是0开始
    for node in range(last_node,-1,-1): #先初始化一个大顶堆
        #print('--node>',node,len(array))
        shift_down(array,node,len(array))
    print('初始堆:',array)
    print('调整堆'.center(30,'-'))
    for i in range(len(array)-1,0,-1):
        tmp = array[i] #暂存最后一个值
        array[i] = array[0] #取最大顶堆的根值(就是列表的第一个值,放在最后面,然后再把其它的列表再进行求大顶堆)
        array[0] = tmp #把列表最后的值 挪到最顶堆的位置

        #上面的转换已经把最顶堆的结构破坏了,也就是说最大堆 现在可能已经不成立了,这时需重构最大堆
        shift_down(array,1,i)
        print(array)
if __name__ == '__main__':
    array = [16,9,21,13,4,11,3,22,8,7,15,29]
    #[3, 4, 9, 15, 21, 7, 13, 8, 11, 16, 22, 29]
    '''array = []
    for i in range(2,50):
        #print(i)
        array.append(random.randrange(1,i))
    '''
    print(array)
    start_t = time.time()
    heap_sort(array)
    end_t = time.time()
    print("cost:",end_t -start_t)
    print(array)