#!/usr/bin/env python3

"""
find_large_assets
~~~~~~~~~~~~~~~~~

A script for finding large assets of an iOS project.

Usage:
    1. Open terminal.
    2. Change directory to your project's root.
    3. Run 'path/find_large_assets.py -n count'.
       'path' is the path from project's root to this script file.
       'count' is the number of assets you want to list.
"""

import os
import config
from argparse import ArgumentParser
from utils import console
from utils import file_assistant


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-n",
        "--number",
        help="number of assets",
        type=int)
    args = parser.parse_args()
    if args.number is None:
        count = config.ASSET_DEFAULT_COUNT
    else:
        count = args.number

    current_path = os.getcwd()
    print('Current directory: ' + current_path)

    assets_paths = file_assistant.get_paths(
        current_path + config.ASSET_PATH_SUFFIX,
        types=config.ASSET_TYPES)

    if not assets_paths:
        console.print_fail('No asset file found!')
        exit(1)

    print('Finding large assets...')
    pairs = dict()
    for asset_path in assets_paths:
        asset_name = file_assistant.file_name(asset_path)
        size = file_assistant.get_size(asset_path)
        pairs[asset_name] = size

    names = [(name, pairs[name])
             for name in sorted(pairs, key=pairs.get, reverse=True)]
    for pair in names[:count]:
        print('name: {}, size {:,.02f} kb.'.format(pair[0], pair[1]))


if __name__ == "__main__":
    main()
