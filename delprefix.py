#coding=utf-8
'''
Created on 2014年11月13日

@author: boring2
'''
import os
import re
def delprefix(prefix,srcdir,destdir=None):
    if os.path.exists(srcdir):
        if destdir == None:
            destdir = srcdir
        elif not os.path.exists(destdir):
            os.mkdir(destdir)
        srcfiles = os.listdir(srcdir)
        for srcfile in srcfiles:
            new_filename = re.sub(prefix, '', srcfile)
            old_path = os.path.join(srcdir,srcfile)
            new_path = os.path.join(destdir,new_filename)
            print(old_path,'->',new_path)
            os.rename(old_path,new_path)
            
    else:
        print('目录不存在')