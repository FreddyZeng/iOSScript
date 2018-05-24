#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import os
import chardet
from argparse import ArgumentParser
"""
输入文件路径替换
~~~~

Usage:
    1. Open terminal.
    2. drag repalce.py to terminal.
    3. drag .string to terminal.
"""

def convert_encoding(filename, target_encoding):
    # Backup the origin file.

    # convert file from the source encoding to target encoding
	with open(filename, 'rb') as source_file:
		content = source_file.read()
		source_encoding = chardet.detect(content)['encoding']
		print(source_encoding)
		if source_encoding != 'utf-8':
			content = content.decode(source_encoding) #.encode(source_encoding)
			if content == None:
				print('the file no text')
				exit()
			with open(filename, 'wb+') as source_file_utf8:
				content = content.encode(target_encoding)
				source_file_utf8.write(content)

def main():
	parser=ArgumentParser()
	parser.add_argument("path",help=".string file path")
	args=parser.parse_args()
	print(args.path)

	convert_encoding(args.path, 'utf-8')

	with open(args.path, 'r+',encoding ='utf-8') as source_file:
		pass
		source_file.write('\n\n// 转换后的:\n\n')

		value = ''
		preline = ''
		for line in source_file:
			#print(line)
			if line.startswith('/*'):
				preline = line
				value = line
				prefix = re.findall('\/\*', line)
				suffix = re.findall('\*\/', line)
				value = value.replace(prefix[0],'')
				value = value.replace(suffix[0],'')
				value = value.replace('\n','')
				value = value.strip()
				continue
			if '=' in line:
				key_value = line
				need_replace_value = re.findall('=.+;', line)
				value_string = '= "{0}";\n'.format(value)
				print(need_replace_value[0])
				key_value = key_value.replace(need_replace_value[0], value_string)
				source_file.write(preline)
				source_file.write(key_value)

if __name__ == "__main__":
    main()
