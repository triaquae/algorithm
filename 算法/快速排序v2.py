# -*- coding: utf-8 -*-


def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        while low < high and array[high] < key:
            #print(low,array[high],key)
            #print(array)
            array[low] = array[high]
            low += 1
            array[high] = array[low]
            #low +=1
    array[low] = key
    return low


def quick_sort(array,low,high):
     if low < high:
        key_index = sub_sort(array,low,high)
        print(array,key_index,array[key_index])
        quick_sort(array,low,key_index)
        quick_sort(array,key_index+1,high)


if __name__ == '__main__':
    #array = [8,10,9,6,4,16,5,13,26,18,2,45,34,23,1,7,3,22,19]
    array = [2, 9, 6, 2, 3, 5, 13, 7, 1, 10, 14]
    print(array)
    quick_sort(array,0,len(array)-1)
    print(array)