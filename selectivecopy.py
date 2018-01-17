#! python3

import os
import sys
import shutil


def selective_copy(folder):
    dest_folder = os.path.abspath('.')

    for foldername, subfolder, files in`
        if not (file_name.endswith('.pdf') or file_name.endswith('.jpg')):
            continue
        else:
            folder_abspath = os.path.abspath(foldername)
            file_name = os.path.join(folder, file_name)
            print('Moving %s, to %s' % (file_name, dest_folder))
            shutil.move(file_name, folder)


def main():
    folder = sys.argv[1]
    selective_copy(folder)


main() 
