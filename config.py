#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# The format of your own localizable method.
# This is an example of '"string".localized'
PREFIX = 'ICXLocalize\(\@'
PREFIX_RAW = 'ICXLocalize(@'
SUFFIX = '\)'
SUFFIX_RAW = ')'
KEY = r'"(?:\\.|[^"\\])*"'
LOCALIZABLE_RE = r'%s%s%s' % (PREFIX, KEY, SUFFIX)

# Specify the path of localizable files in project.
LOCALIZABLE_FILE_PATH = ''
LOCALIZABLE_FILE_NAMES = ['Localizable']
LOCALIZABLE_FILE_TYPES = ['strings']

# File types of source file.
SEARCH_TYPES = ['swift', 'm', 'json']
SOURCE_FILE_EXCLUSIVE_PATHS = []
LOCALIZABLE_FILE_EXCLUSIVE_PATHS = []

LOCALIZABLE_FORMAT_RE = r'"(?:\\.|[^"\\])*"\s*=\s*"(?:\\.|[^"\\])*";\n'


SourceFileALL_TARGET_PATH = 'SourceFileAll.strings' # 项目中所有的key

DEFAULT_TARGET_PATH = 'noTranslation.strings' # 未翻译的字符串文件路径

DIDTRANSLATION_TARGET_PATH = 'didTranslation.strings' # 已经翻译的字符串文件路径


CHANGE_PREFIX = 'NSLocalizedString(@'
CHANGE_SUFFIX = ')'
ISCHANGE = True #是否替换
