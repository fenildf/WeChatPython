#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''调用Microsoft Azure的AI接口'''

__author__ = "jiegl"

from dispose import dispose 

def main():
	disposeObj = dispose()
	reply = disposeObj.run("登陆错误怎么办")
	print(reply)

if __name__ == '__main__':    
	main()
