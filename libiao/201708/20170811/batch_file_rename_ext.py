#!/usr/bin/python
# -*- coding:utf-8 -*-
# batch_file_rename.py
# Created: 6th August 2012

'''
This will batch rename a group of files in a given directory,
once you pass the current and new extensions
不修改子目录下文件后缀
'''
import os
import sys
import argparse


def batch_rename(work_dir, old_ext, new_ext):
    '''
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    '''
    # files = os.listdir(work_dir)
    for filename in os.listdir(work_dir):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        print "file_ext is :",file_ext
        print "filename is :",filename
        # Start of the logic to check the file extensions, if old_ext = file_ext
        if old_ext == file_ext:
            print "old_ext =file_ext:",old_ext
            # Returns changed name of the file with new extention
            name_list = list(filename)
            print "name_list is :",name_list
            name_list[len(name_list) - len(old_ext):] = list(new_ext)
            print "name_list len is :",len(name_list)
            print "old ext len is :",len(old_ext)
            newfile = ''.join(name_list)
            print "new file is :",newfile
            # Write the files
            os.rename(
                os.path.join(work_dir, filename),
                os.path.join(work_dir, newfile)
            )


def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser


def main():
    '''
    This will be called if the script is directly invoked.
    '''
    # adding command line argument
    parser = get_parser()
    args = vars(parser.parse_args())

    # Set the variable work_dir with the first argument passed
    work_dir = args['work_dir'][0]
    # Set the variable old_ext with the second argument passed
    old_ext = args['old_ext'][0]
    # Set the variable new_ext with the third argument passed
    new_ext = args['new_ext'][0]

    batch_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
