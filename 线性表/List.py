'''
在Python中，list和tuple就可以看作是线性表的实现,
线性表是一种逻辑结构，表示元素之间的一一的相邻关系，顺序表和链表是指存储结构
'''
list1 = list([1,2,3,4,5])    #创建新表

list1.append(6)              #在尾部添加新元素 6

k = len(list1)               #返回表长度
list1.insert(k,7)            #在位置k插入7

list1.pop()                  #返回并删除尾部元素
print(list1)                 #输出表的全部元素

list2 = list1[2:]            #表的切片操作
print(list2)

list1.remove(1)   #删除一个元素
print(list1)
