from bs4 import BeautifulSoup
from urllib.error import URLError,HTTPError
import os,socket
import urllib.request
path = os.getcwd()
new_path = os.path.join(path,"meizhi")
if not os.path.exists(new_path):
    os.mkdir(new_path)

Homeurl = 'http://www.dbmeizi.com'
try:
    content = urllib.request.urlopen('http://www.dbmeizi.com',timeout=20).read().decode('utf-8')
except socket.timeout as e:
    print("网速太慢了，请重试")
    print(e)
#先访问下主页，获得总页数,cgidata.page_count=370;,这个cgidata.page_count保存的是总页数
index_begin = content.find('cgidata.page_count=')
#f = open('html.txt','w',encoding='utf-8')
#print(content,file=f)
#f.close()
#print(index_begin)
index_begin += len('cgidata.page_count=')
#print(index_begin)
index_end = content.find(';',index_begin)
print(index_begin)
print(index_end)
PageCount = content[index_begin:index_end]#截取总页数
nPageCount = int(PageCount,10)
print(nPageCount)
#循环访问页面下载图片
#页面的地址格式http://www.dbmeizi.com/?p=0
for page in range(10):
    print('正在下载第%d页' % page)
    Pageurl = 'http://www.dbmeizi.com/?p=%d' % page
    try:
        content_1 = urllib.request.urlopen(Pageurl,timeout=20).read().decode('utf-8')
    except:
        print("该页异常下一页")
        continue #出现异常跳到下一页
    soup = BeautifulSoup(content_1)
    picUrls = soup.find_all('img')
    for girlUrl in picUrls:
        girlLink = girlUrl.get('src')
        print(girlLink)
        try:
            content_2 = urllib.request.urlopen(girlLink,timeout=20).read()
            f= open('meizhi//' + girlLink[-15:],'wb')
            f.write(content_2)
        except:
            print("该张图片异常，下一页")
            continue
print('下载完毕，按回车键退出')
input()
            
                                                                                        
