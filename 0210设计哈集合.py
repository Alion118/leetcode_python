# -*- coding: utf-8 -*-
# @Time    : 2019/2/10 20:53
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
# HashMap是一个用于存储Key-Value键值对的集合，
# 每一个键值对也叫做Entry。
# 这些个键值对（Entry）分散存储在一个数组当中，这个数组就是HashMap的主干。
# python中的这些东西都是哈希原理：字典(dictionary)、集合(set)、
# 计数器(counter)、默认字典Defaut dict)、有序字典(Order dict).
class MyHashSet(object):
	def __init__(self):
		self.t=[-1]*1000000
	def add(self,key):
		self.t[key]=1
	def remove(self,key):
		self.t[key]=-1
	def contains(self,key):
		return self.t[key]==1

h=MyHashSet()
h.add(2)
h.add(3)
h.remove(2)
print(h.contains(2))
