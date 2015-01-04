import os
def renamefile(prefix,srcdir,destdir=NULL):
    '''
    prefix定义前缀,
    srcdir为源目录,
    destdir定义目的目录
    '''
    if os.path.exists(srcdir):
        if destdir == NULL:
            destdir = srcdir
        elif not os.path.exists(destdir):
            os.mkdir(destdir)
        for srcfile in srcfiles:
            #filename,sufix = os.path.splitext(srcfile)
            #print(filename,sufix)
            new_filename = prefix + srcfile
            old_path = os.path.join(srcdir,srcfile)
            new_path = os.path.join(destdir,new_filename)
            #print(old_path)
            #print(new_path)
            os.rename(old_path,new_path)
    else:
        print('源目录不存在')
