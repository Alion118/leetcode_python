# -*- coding: utf-8 -*-
# @Time    : 2019/3/10 20:48
# @Author  : Linder
# @Email   : lmj2018666@gmail.com
# @Software: PyCharm
n = int(input())
for i in range(1,n+1,2):
	print(i, end=' ')
l= list(range(0,n+1,2))[1:]
if n%2!=0:
	l=l[1:]+[l[0]]

while (n//2+1)-1:
	try:
		print(l[0],end = ' ')
		l = l[2:]+[l[1]]
	except:
		break