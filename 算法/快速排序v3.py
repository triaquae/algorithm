#_*_coding:utf-8_*_
__author__ = 'Alex Li'


def quick_sort(array, k_index,low,high):
    '''

    :param array:
    :param low: 列表的第一个索引
    :param high: 列表最后一个元素的索引
    :return:
    '''
    k = array[k_index]
    print('*'*50)
    print("sub list:",array[k_index:])
    print("k_index:%s, low:%s,high:%s" %(k_index,low,high) )
    while low < high:
        #先从右边开始找起

        while low < high and array[high] >k:#一直loop直到找到一个右边的值 比 k大的值 的
            high -=1
        #上面这个loop停止了的话,代表列表找了一遍了,或者找到了一个比k小的值
        #此时high可能正指向了那个比k小的值 ,应该把这个值换到k左边
        #换到左边放哪呢? 不要占用k所在的值 现在,
        #print('high:',array[high])
        #现在从列表左边开始找比 k大的值 ,直到找到为止,或者是遇到high也停止, 因为high右边没有比k大的了(上面已经找过了)
        while low < high and array[low] < k :
            low +=1
        #当上面这个loop停止了,代表low遇到了high,或者找到了一个比k大的值
        #此时low 应该是指向了10, high指向了3, [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3,22,19]
        #接下来把low和high做个对调
        if low <high:#如果他俩相等,代表 loop都 过了一遍了
            tmp = array[high]
            array[high] = array[low]
            array[low] =  tmp
        else:#如果low不小于high了,只能代表一种情况,就是low and high相遇了,如果相遇,就把k的值 赋值到相遇的地方,(跟相遇的位置 的值做个对调)
            array[k_index] = array[low]
            array[low] = k
            #k_index +=1
            #pass
            #代表 列表 已经 按关键k的值 ,分成了两部分了,比k小的在k左边,比k大的在k右边
            #if len(array[:low]) > 1:
            #    quick_sort(array,k_index,k_index+1,low) #把左边的再去排序
            #if len(array[low:])>1:
            #    print("for high")
            #    quick_sort(array,high,low+1,len(array[low:])) #把右边的再去排序
    print(low,high,array)
    return low


if __name__ == '__main__':

    #array = [14,10,9,6,99,16,5,13,26,18,2,45,34,23,1,7,3,22,19,2]
    array = [ 2, 9, 6, 2, 3, 5, 13, 7,1, 10, 14]
    array_before_sort =[14,10,9,6,99,16,5,13,26,18,2,45,34,23,1,7,3,22,19,2]
    key_index = quick_sort(array,0,1,len(array)-1)

    print('key_index:',key_index)

    print("-------final -------")
    print(array_before_sort)
    print(array)
