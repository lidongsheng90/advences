#-*- coding:utf-8 -*-
__author__ = 'lds'
__date__ = '2019/3/26 10:34'

import sys
import os
import fnmatch
import shutil

def move_file(source_dir,dst_dir,file_list):
    for parent,dirs,filenames in os.walk(source_dir):
        for file in filenames:
            #print (file)
            for file_type in file_list:
                if fnmatch.fnmatch(file,file_type):
                    dirs=parent.replace(source_dir,dst_dir)
                    if not os.path.exists(dirs):
                        os.makedirs(dirs)
                    if os.path.exists(dirs+'\\'+file):
                        os.remove(dirs+'\\'+file)
                    else:
                        shutil.move(os.path.join(parent+'\\'+file),dirs)
            #print(parent.replace(rootdir,dst_dir))
            #print (os.path.join(parent+'\\'+file))

if __name__=='__main__':
    source_dir = r'D:\a1'
    dst_dir = r'D:\a2'
    move_file(source_dir,dst_dir,['*.txt','*.json'])
    print ("successful")






