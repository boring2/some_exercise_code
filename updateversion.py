#coding=utf-8
#刷版本号的脚本
import glob,os,sys
def modifyVersion(version,srcfolder):
    if os.path.exists(srcfolder):
        filelist = [efile.replace('\\','/') for efile in glob.glob(srcfolder+'/*.json')]
        for file in filelist:
            content = []
            with open(file) as f:
                for eline in f:
                    if '"Version": ' in eline:
                        num = eline.strip().split(":")[1]
                        num = num[1:3]
                        eline = eline.replace(num,version)
                        content.append(eline)
                    else:
                        content.append(eline)
            with open(file,'w') as f:
                f.writelines(content)
            
    else:
        print("have not this folder")
        
if __name__ == '__main__':
    if len(sys.argv) != 3:
            print('usage:need two args.\nexample:python shuaversion.py 14 F:/python3.4/code/peizhibiao')
    else:
        #srcfolder = r'F:/python3.4/code/配置表20141224'
        modifyVersion(sys.argv[1],sys.argv[2])
        print('success')
        