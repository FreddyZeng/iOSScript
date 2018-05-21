#!/usr/bin/env python3

"""
i18n
~~~~

A script for internationalization in iOS projects.

Usage:
    1. Open terminal.
    2. Change directory to your project's root.
    3. Run 'path/i18n.py'.
    4. Run 'path/i18n.py -h' for more usage.

    'path' is the path from project's root to this script file.
"""

import os
import re
import config
from argparse import ArgumentParser
from subprocess import call
from utils import console
from utils import file_assistant


def _should_skip_line(line):
    return line == '\n' or line.startswith('//')


def _check_localiztion_format_files(file_paths):
    is_good_format = True
    for path in file_paths:
        is_good_format = _check_localiztion_format(path) and is_good_format
    if not is_good_format:
        console.print_fail('Checking localizable file failed.')
        exit(1)

# 检测localiztion是不是好格式
def _check_localiztion_format(file_path):
    is_good_format = True
    with open(file_path, 'r') as source_file: # 尝试用open 打开file 如果成功打开文件，就是source_file.   'r'是以只读的形式打开
        for index, line in enumerate(source_file):# 遍历文件的行号
            if _should_skip_line(line):# 如果是注释，则跳过该行
                continue
            if not re.match(config.LOCALIZABLE_FORMAT_RE, line):# 如果localiztion 中的行翻译不合法 "" = "";就不是好格式，返回false
                console.print_warning('Error format in file:\n{}, line: {}'
                                      .format(file_path, index + 1))
                is_good_format = False
    return is_good_format


def _remove_duplicate_strings_files(file_paths):
    for path in file_paths:
        _remove_duplicate_strings(path)


def _remove_duplicate_strings(file_path):
    keys = []
    lines = []
    with open(file_path, 'r') as source_file:
        for line in source_file:
            if _should_skip_line(line):
                keys.append('')
                lines.append(line)
            else:
                matchs = re.findall(config.KEY_RE, line)
                if matchs:
                    key = matchs[0]
                    if key not in keys:
                        keys.append(key)
                        lines.append(line)
                    else:
                        index = keys.index(key)
                        lines[index] = line
                        print('Duplicate key found in file:\n'
                              '%s line: %s' % (file_path, key))
    with open(file_path, 'w') as source_file:
        source_file.writelines(lines)


def _add_new_strings(old_files, new_files):
    new_string_paths = file_assistant.get_paths(
        new_files, names=config.LOCALIZABLE_FILE_NAMES)
    _check_localiztion_format_files(new_string_paths)
    _remove_duplicate_strings_files(new_string_paths)
    for path in new_string_paths:
        language = path.split('/')[-2]
        for old_path in old_files:
            if language in old_path:
                with open(old_path, 'a') as old_file:
                    with open(path, 'r') as new_file:
                        for line in new_file:
                            old_file.write(line)
    console.print_bold('%d localizable strings files added.'
                       % len(new_string_paths))


def _get_project_path(args):
    if args.path is None:
        return os.getcwd() # 返回当前工作目录。
    else:
        return args.path


def _get_target_path(args):
    if args.output is None:
        return os.path.join(os.getcwd(), config.DEFAULT_TARGET_PATH)
    else:
        target_path = args.output
        try:
            target = open(target_path, 'w')
            target.close()
        except OSError:
            console.print_fail('Error: Invalid file path %s' % target_path)
            exit(1)
        return target_path


# 获取所有的文件路径
def _get_source_file_paths(path):
    source_file_paths = file_assistant.get_paths(
        path,# 文件路径
        types=config.SOURCE_FILE_TYPES,# 文件类型
        exclusive_paths=config.SOURCE_FILE_EXCLUSIVE_PATHS)# 排除文件路径
    if not source_file_paths:
        console.print_fail(
            'No source file found!\n'
            'Please change your current directory to project\'s root.')
        exit(1)
    return source_file_paths


# 获取本地字符串的多语言翻译文件路径
def _get_localization_paths(path):
    localization_paths = file_assistant.get_paths(
        os.path.join(path, config.LOCALIZABLE_FILE_PATH),# 获取LOCALIZABLE的文件夹
        names=config.LOCALIZABLE_FILE_NAMES,# 获取LOCALIZABLE的文件名字
        types=config.LOCALIZABLE_FILE_TYPES,# 获取LOCALIZABLE的文件拓展名
        exclusive_paths=config.LOCALIZABLE_FILE_EXCLUSIVE_PATHS)# 获取LOCALIZABLE排除的文件夹
    if not localization_paths:
        console.print_fail('No localization file found!')
        exit(1)# 没有找到localization_paths
    return localization_paths


def _get_all_localization_strings(path):
    all_localization_strings = set()
    for path in path:
        with open(path, 'r') as source_file:
            for line in source_file:
                strings = re.findall(config.LOCALIZABLE_RE, line)# 在一行中，查找所有.local的字符串
                for string in strings:
                    name = string.replace(
                        'ICXLocalize(@',
                        '')# 去掉前缀
                    name = name.replace(
                        config.LOCALIZABLE_SUFFIX,
                        '')# 去掉后缀
                    all_localization_strings.add(name)
    return all_localization_strings # 返回所有文字


def _find_unlocalized_strings(strings, paths):
    unlocalized_strings = set()
    for name in strings:
        for path in paths:
            if file_assistant.file_contains(path, r'{}'.format(name)):
                # 如果path的.localizable文件中，存在key了，则是已经添加
                continue
            else:
                #否则中止循环，添加到为未翻译的数组
                break
        else:
            continue
        unlocalized_strings.add(name)
    return unlocalized_strings


def _generate_unlocalized_strings_file(strings, path):
    with open(path, 'w') as target:
        for name in sorted(strings):
            target.write('{0} = {0};\n'.format(name))
    call(['open', path])
    print('%d unlocalized strings found.' % len(strings))
    console.print_bold('Generated strings path: %s' % path)


def _get_args():
    parser = ArgumentParser()
    parser.add_argument(
        "-i",
        "--integrate",
        help="Integrate new localizable strings.",
        type=str)
    parser.add_argument(
        "-o",
        "--output",
        help="Set output file path.",
        type=str)
    parser.add_argument(
        "-p",
        "--path",
        help="Set project path.",
        type=str)
    parser.add_argument(
        "-r",
        "--remove",
        help="Remove duplicate localizable strings.",
        action='store_true')
    return parser.parse_args()


def main():
    args = _get_args()# 获取args 参数

    project_path = _get_project_path(args)# 从命令行获取参数。如果不存在path，就使用当前终端的路径
    print('Current directory: ' + project_path) # 打印当前目录

    print('Checking localizable files...')
    localization_paths = _get_localization_paths(project_path)# 递归获取项目中的所有localization文件路径
    _check_localiztion_format_files(localization_paths)# 检测所有的localization，看看是不是都以 "" = "";表示

    if args.remove:
        print('Removing duplicate localizable strings...')
        _remove_duplicate_strings_files(localization_paths)

    if args.integrate is not None:
        print('Adding new localizable strings...')
        _add_new_strings(localization_paths, args.integrate)
        exit(0)

    print('Finding unlocalized strings...')
    source_file_paths = _get_source_file_paths(project_path)# 得到所有文件源文件的路径
    all_localization_strings = _get_all_localization_strings(source_file_paths)# 获取所有的翻译字符串
    unlocalized_strings = _find_unlocalized_strings(all_localization_strings,
                                                    localization_paths) # 传入一个数组所有需要翻译的字符串，传入iOS项目工程根目录，
    # 返回所有未翻译的文字unlocalized_strings

    if not unlocalized_strings:
        console.print_bold('No unlocalized string found.')
    else:
        target_path = _get_target_path(args)# 找到了还没翻译的key，获取key导出的路径
        _generate_unlocalized_strings_file(unlocalized_strings, target_path)# 把需要翻译的key 写出到


if __name__ == "__main__":
    main()
