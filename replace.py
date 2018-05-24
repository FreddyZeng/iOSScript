#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import re
import os
from argparse import ArgumentParser
"""
输入文件路径替换
~~~~

Usage:
    1. Open terminal.
    2. drag repalce.py to terminal.
    3. drag .string to terminal.
"""

def main():
	parser=ArgumentParser()
	parser.add_argument("path",help=".string file path")
	args=parser.parse_args()
	print(args.path)
	with open(args.path, 'r+',encoding ='UTF-16') as source_file:
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
