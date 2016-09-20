#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import random
import time

def heap_adjust(array,node_index):
    '''
    调用一个局部二叉堆为大最大堆
    :param node_index: 此处的node_index 是需要减1才能跟列表中的实际下标对应上的噢
    :return:
    '''


    node_right_child_index = (node_index*2+1) -1
    while node_right_child_index < len(array):
        node = array[node_index-1] #
        left_child = array[node_index*2 -1]
        right_child = array[(node_index*2+1) -1]
        #print(node,left_child,right_child)
        #tmp = node #先把父亲存个临时变量
        if node < left_child: #和左孩子 交换
            array[node_index-1] = left_child
            array[node_index*2 -1] =  node
            #print("less than left:", node,left_child)
        elif node < right_child: #
            array[node_index-1] = right_child
            array[(node_index*2+1)-1] = node
            #print("less than right:", node,right_child)

        if  node >= left_child or node >= right_child:#已实现最大堆
            '''print('perfect',
                  array[node_index-1],
                  array[node_index*2 -1],
                  array[(node_index*2+1)-1])
            '''
            break
        #print('keep...')
def build_heap(array):
    i = int(len(array) / 2) #非叶子节点个数
    #while i > 0: #先生成初始堆
    #    heap_adjust(array,i ) #初始最大堆
    #    i -=1

    k = len(array) -1 #接下来再调整堆
    while k>0:


        i = int(k / 2) #非叶子节点个数
        #index = i - 1 #堆排序序列下标是从1开始,但列表 是从0开始
        while i > 0:
            index = i - 1
            node_val = array[index] #堆顶节点值
            #left_node_val = array[2*i-1]
            #right_node_val = array[(2*i+1)-1]
            #print(node_val,left_node_val,right_node_val)
            heap_adjust(array,i )
            #print('------',i)
            i -=1

        #取最大顶堆的根值(就是列表的第一个值,放在最后面,然后再把其它的列表再进行求大顶堆)
        tmp = array[0]
        array[0] = array[k]
        array[k] = tmp
        k-=1



if __name__ == '__main__':
    #array = [16,9,21,22,13,4,11,3,22,9,15,8]
    array = []
    for i in range(1,5000):
        #print(i)
        array.append(random.randrange(i))
    print(array)
    start_t = time.time()
    build_heap(array)
    end_t = time.time()
    print("cost:",end_t -start_t)
    print(array)