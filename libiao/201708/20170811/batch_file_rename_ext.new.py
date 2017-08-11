#!/usr/bin/python
# -*- coding:utf-8 -*-
'''
批量修改指定目录下：以特定ext结尾的文件，变更为新的后缀文件，如将/tmp/ 以unl结尾的文件全部变更为 .txt文件
usage：如：bath_file_ext_rename_new.py /tmp .unl .txt 将/tmp目录下所有以unl为后缀的文件，修改为.txt文件'
created: libiao 2017-08-11
'''

import  os
import  sys

def batch_rename(work_dir,old_ext,new_ext):
    '''获得指定目录下的所有文件以及目录名称'''
    for filename in os.listdir(work_dir):
        file_ext=os.path.splitext(filename)[1]
        file_name=os.path.splitext(filename)[0]
        if file_ext == old_ext:
            print "into file_ext == old_ext"
            new_file=file_name+new_ext
            os.rename(os.path.join(work_dir,filename),os.path.join(work_dir,new_file))
def main():
    work_dir=sys.argv[1]
    old_ext=sys.argv[2]
    new_ext=sys.argv[3]
    print "work_dir is :",work_dir
    print "old_ext is :",old_ext
    print "new_ext is :",new_ext
    batch_rename(work_dir, old_ext, new_ext)
if __name__ == '__main__':
    main()

