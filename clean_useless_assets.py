#!/usr/bin/env python3

"""
clean_useless_assets
~~~~~~~~~~~~~~~~~~~~~

A script for cleaning useless assets of an iOS project.

Usage:
    1. Open terminal.
    2. Change directory to your project's root.
    3. Run 'path/clean_useless_assets.py'.
       'path' is the path from project's root to this script file.
"""

import os
import shutil
import config
from utils import console
from utils import file_assistant


def main():
    current_path = os.getcwd()
    print('Current directory: ' + current_path)

    possible_reference_paths = file_assistant.get_paths(
        current_path,
        types=config.ASSET_SOURCE_FILE_TYPES,
        exclusive_paths=config.SOURCE_FILE_EXCLUSIVE_PATHS)

    assets_paths = file_assistant.get_paths(
        current_path + config.ASSET_PATH_SUFFIX,
        types=config.ASSET_TYPES)

    if not possible_reference_paths:
        console.print_fail(
            'No source file found!\n'
            'Please change your current directory to project\'s root.')
        exit(1)

    if not assets_paths:
        console.print_fail('No asset file found!')
        exit(1)

    print('Finding useless assets...')

    total_size = 0
    total_count = 0
    for asset_path in assets_paths:
        asset_name = file_assistant.file_name(asset_path)
        for file_path in possible_reference_paths:
            with open(file_path, 'r', encoding='latin1') as source_file:
                for line in source_file:
                    if asset_name in line:
                        break
                else:
                    continue
                break
        else:
            size = file_assistant.get_size(asset_path)
            total_size += size
            total_count += 1
            print('Removing {} ({:,.02f} kb) ...'.format(asset_name, size))
            shutil.rmtree(asset_path)

    if not total_count:
        console.print_bold('No useless assets needs to be removed.')
    else:
        console.print_bold(
            '\n{} useless assets have been removed.\n'.format(total_count)
            + 'Total size {:,.02f} kb.'.format(total_size))


if __name__ == "__main__":
    main()
