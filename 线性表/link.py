# -*- coding: utf-8 -*-
# 参考：https://www.cnblogs.com/ybf-yyj/p/8574748.html
# 定义每个节点

class Node:
	
	def __init__(self, data):
		self.data = data
		self.next = None


class linkList(object):

	"""初始化头结点"""
	def __init__(self, n):
		self.head = Node(None)
		self.n = n

	""" 头插法建立链表 头结点->new新节点->节点"""
	def listCreateForward(self):
		if self.n == 0:
			return False
		else:
			temp = self.head
			for i in range(1, self.n+1):
				print('请输入第{0}个节点：'.format(i))
				num = input()
				node = Node(int(num))
				node.next = temp.next
				temp.next = node

	""" 尾插法建立链表 头结点(头结点的数据域可以存储链表长度)->首元结点(存数据的第一个节点)->节点->new新节点"""	
	def listCreateBackward(self):
		if self.n == 0:
			return False
		else:
			temp = self.head
			for i in range(1, self.n+1):
				print('请输入第{0}个节点：'.format(i))
				num = input()
				node = Node(int(num))  # 需要对输入的类型转换，参考https://blog.csdn.net/weixin_40283816/article/details/86634273?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
				temp.next = node
				temp = node
	
	""" 读取链表 """
	def readList(self):
		if self.n == 0:
			print('空链表')
		else:
			temp = self.head
			while  temp.next != None:
				temp = temp.next
				print(temp.data)

	""" 链表长度 """
	def Length(self):
		i = 0
		temp = self.head
		while temp.next != None:
			temp = temp.next
			i += 1

		return i

	""" 按值查找 """
	def locateElem(self, num):
		i = 0
		temp = self.head
		while temp.next != None:
			temp = temp.next
			i += 1
			if int(temp.data) == num:
				return i
		return None


	""" 按位置查找 """
	def getElem(self, j):
		i = 0
		temp = self.head
		while temp.next != None:
			temp = temp.next
			i += 1
			if int(j) == i:
				return temp.data
		return None


	""" 按位置插入数字 """
	def listInsert(self, j, num):
		if int(j) < 0:
			return None
		elif self.Length() < j:
			return None
		else:
			i = 0
			temp = self.head
			while temp.next != None:
				i += 1
				if int(j) == i:
					node = Node(num)
					node.next = temp.next
					temp.next = node
				temp = temp.next


	""" 删除特定元素 """
	def deleteData(self, num):
		temp = self.head
		while True:
			if temp.next == None:
				break
			if int(temp.next.data) == num and temp.next.next == None: # 当这个节点是尾结点时
				temp.next = None
				break
			elif int(temp.next.data) == num:
				temp.next = temp.next.next
			temp = temp.next

	""" 删除特定位置元素 """
	def deleteElem(self, j):
		if j == 1:
			self.head.next = self.head.next.next
		elif j == self.Length():
			temp = self.head.next
			while True:
				if temp.next.next == None:
					temp.next = None
					break

				temp = temp.next
		elif j < self.Length():
			i = 2
			temp = self.head.next
			while True:
				if i == j:
					temp.next = temp.next.next
		else:
			print('error!')
			return None


# 创建一个具有5个节点的链表
linklist1 = linkList(5)
linklist1.listCreateBackward()
linklist1.readList()





