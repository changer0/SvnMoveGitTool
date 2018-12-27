#!/usr/bin/python
# -*- coding: utf-8 -*-
import io,os,sys,time,string,subprocess,importlib

importlib.reload(sys)
#sys.setdefaultencoding('utf8')

success_list = []
fail_list = []
with open("source.txt") as f:
	while True:
		a_line = f.readline()
		if (a_line == ""):
			break
		if (a_line.find('>') > 0):
			source, target = a_line.split('>')
			source = source.strip()
			target = target.strip()
			if (source.endswith('/')):
				source = source[:-1]
			pos=source.rfind("/")
			name=source[pos+1:]
			print("source:" + source)
			print("target:" + target)
			print("name:" + name)
			if (source == ""):
				print("原SVN路径为空，迁移失败！请检查source.txt内容是否正确！")
				continue
			if (target == ""):
				print("目标仓库路径为空，迁移失败！请检查source.txt内容是否正确！")
				fail_list.append(source)
				continue
			#这个地方取得最后的tag name
			#strList = source.split("/")
			
			#tagName = strList[len(strList) - 1]
			#print("tagName: " + tagName)
			res = subprocess.call(["sh", "transfer.sh", source, target, name])
			if (res != 0):
				fail_list.append(source)
			else:
				success_list.append(source)

print(" ##^v^## Move Finished，Success: %d，Failed: %d" % (len(success_list), len(fail_list)))
if (len(fail_list) > 0):
	i = 1
	for source in fail_list:
		print("##￣へ￣## Failed Path: %d：%s" % (i, source))
		i = i+1
