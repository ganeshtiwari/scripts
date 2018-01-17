#!/usr/bin/env python3

import os
import sys


def delete_file(folder, file_size):
    """
    Deletes files greater or equal to file_size in the dir_tree
    """
    folder_abspath = os.path.abspath('.')

    for foldername, subfolders, files in os.walk(folder):
        for file_name in files:
            print(file_name)
            current_folder_abspath = os.path.abspath(foldername)
            file_name = os.path.join(current_folder_abspath, file_name)
            if os.path.getsize(file_name) >= file_size:
                print('Removinng %s' % (file_name))
                os.remove(file_name)


def main():
    folder, file_size = sys.argv[1], int(sys.argv[2])
    delete_file(folder, file_size)


main()
