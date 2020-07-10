# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 11:20
# @Author  武兴来
# @email: 264695688@qq.com
#冒泡排序定义:一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢"浮"到数列的顶端
#个人理解:遍历所有数列，按照顺序进行调换位置，然后依次重排序

list = [100,45,78,99,33,23,6,3,2,6,7,1]

'''1.len(list)) 是list 长度 .index 表示索引，list[index]表示取出对应list的值；
#2.索引本身赋值范围是list[-len(list)] <= index <= list[len(list)-1]
'''

for i in range(len(list)):
        for j in range(i+1,len(list)):
              if list[i] > list[j]: # <按照从大到小，>按照从小到大
                 list[i],list[j] = list[j],list[i] #调换赋值
        print(list)


#参考地址:
#https://www.runoob.com/python3/python-bubble-sort.html 

