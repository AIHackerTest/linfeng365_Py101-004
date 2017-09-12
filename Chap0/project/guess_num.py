# -*- coding: utf-8 -*-

import random
def main():
	b = random.randint(0,20)
	print ("已经生成一个数,猜猜是多少?")


#	print (b)
	
	n = 0
	m = 10
	panduan(b,n,m)
def panduan(x,n,m):
	a = int(input()) # 转换为一个整数。int(x [,base]) http://www.runoob.com/python/python-variable-types.html

	if a>x:
		print ("大了")
		n=n+1
		print ("你还有 %s 次机会" % (m-n))
		panduan(x,n,m) # 递归调用

	elif a<x :
		print("小了")
		n=n+1
		print ("你还有 %s 次机会" % (m-n))
		panduan(x,n,m) # 递归调用

	else:
		n=n+1
		print ("正确!这个数就是 %s" % x)
		print ("你一共猜了%s次"%n)



if __name__== '__main__':
	main()