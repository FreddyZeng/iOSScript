#!/usr/bin/env python3

SOURCE_FILE_TYPES = ['swift', 'json', 'm']
SOURCE_FILE_EXCLUSIVE_PATHS = ['Pods']

LOCALIZABLE_FILE_PATH = 'Meum/MeumFoundation/BaseObject/Resource/InternationalFile/en.lproj'
LOCALIZABLE_FILE_NAMES = ['Localizable']
LOCALIZABLE_FILE_TYPES = ['strings']
LOCALIZABLE_FILE_EXCLUSIVE_PATHS = None
LOCALIZABLE_SUFFIX = ')'
DEFAULT_TARGET_PATH = 'generated.strings' # 查找到尚未翻译的key，输出到当前工程的该相对路径下

LOCALIZABLE_RE = r'ICXLocalize\(\@".*?"\)' # 查找源文件中的多语言翻译的正则



KEY_RE = r'"(?:\\.|[^"\\])*"'
LOCALIZABLE_FORMAT_RE = r'"(?:\\.|[^"\\])*" = "(?:\\.|[^"\\])*";\n' # LOCALIZABLE 文件中的翻译匹配


ASSET_TYPES = ['imageset', 'mp3', 'mp4', 'ttf', 'otf']
ASSET_SOURCE_FILE_TYPES = ['swift', 'm', 'json', 'xib',
                           'storyboard', 'js', 'map', 'plist']
ASSET_PATH_SUFFIX = '/DeviceManager/Class/Anima'
ASSET_DEFAULT_COUNT = 50
