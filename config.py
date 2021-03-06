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

SOURCE_FILE_EXCLUSIVE_PATHS = [] #这个数据内的文件夹，不进入搜索源文件
LOCALIZABLE_FILE_EXCLUSIVE_PATHS = [] #这个数据内的文件夹，不进入搜索LOCALIZABLE文件

LOCALIZABLE_FORMAT_RE = r'"(?:\\.|[^"\\])*"\s*=\s*"(?:\\.|[^"\\])*";\n'


SourceFileALL_TARGET_PATH = 'SourceFileAll.strings' # 项目中所有的key

DEFAULT_TARGET_PATH = 'noTranslation.strings' # 未翻译的字符串文件路径

DIDTRANSLATION_TARGET_PATH = 'didTranslation.strings' # 已经翻译的字符串文件路径


SourceFileALL_TARGET_PATH = 'SourceFileAll.strings' # 项目中所有的key


CHANGE_PREFIX = 'NSLocalizedString(@'
CHANGE_SUFFIX = ')'
ISCHANGE = False #是否替换
DEFAULT_TARGET_PATH = 'noTranslation.strings' # 未翻译的字符串文件路径
DIDTRANSLATION_TARGET_PATH = 'didTranslation.strings' # 已经翻译的字符串文件路径

FINDCHINESE_INOC_TARGET_PATH = 'findChineseInOC.strings' #  寻找项目中文件存在的中文参数
FINDCHINESE_INSWIFT_TARGET_PATH = 'findChineseInSwift.strings' #  寻找项目中文件存在的中文参数
ISFINDCHINESE = True

FINDCHINESE_RE = '"@[^"]*[\u4E00-\u9FA5]+[^"\n]*?"'
FINDCHINESE_SWIFT_RE = '"[^"]*[\u4E00-\u9FA5]+[^"\n]*?"'
FINDCHINESE_EXCLUSIVE_TEXT = ['NSAssert', 'Assert', 'Log', 'NSError', 'NSException', 'imageNamed:', 'UIImage.init(named:', 'UIImage(named:', 'print']

ASSET_TYPES = ['imageset', 'mp3', 'mp4', 'ttf', 'otf']
ASSET_SOURCE_FILE_TYPES = ['swift', 'm', 'json', 'xib',
                           'storyboard', 'js', 'map', 'plist']
ASSET_PATH_SUFFIX = '/car8891'
ASSET_DEFAULT_COUNT = 50