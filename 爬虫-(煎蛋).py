import requests
import re
import os
from pyquery import PyQuery as pq



#获取http://www.haopic.me/tag/meizitu的html
def get_text():
    main_url = 'http://www.haopic.me/tag/meizitu'
    try:
        r = requests.get(main_url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(1)
        return r.text
    except:
        return '0'
    
#解析http://www.haopic.me/tag/meizitu并得到所有妹子图的url
def parse_text(html):
    doc = pq(html)
    lis = doc('#mainbox .item_list .item_box h2').items()
    for li in lis:
        
        href = re.search('[a-zA-Z]+://[^\s]*', li.html())
        #print(href.group()[:-1])
        url.append(href.group()[:-1])

def get_page(scd_url):
   
    #Referer = 'http://www.haopic.me/'
    
    #url = Referer + str(page)
    
    try:
        r = requests.get(scd_url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        
        #print(1)
        return r.text
    except:
        return '0'

def parse_page(html):
    #pyquery
    doc = pq(html)
    ps = doc('.content-c p').items()
    for p in ps:
        img = p.html()
        #print(img)
        src = re.search('[a-zA-Z]+://[^\s]*', img, re.S)
        num = re.search('\d*\.(jpg|jpeg)', img, re.S)
        image_url = src.group()[:-1]
        #print(image_url)
        images_url.append(image_url)

def save_image(new_url):
    #if not os.path.exists(str(new_url.split('/')[-1])):
        #os.mkdir(str(new_url.split('/')[-1]))
    try:
        r = requests.get(new_url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        file_path = new_url.split('/')[-1]
        if not os.path.exists(str(new_url.split('/')[-1])):
            with open(file_path, 'wb') as f:
                f.write(r.content)
                print('保存成功')
        else:
            print('Already Exists')
    except:
        return '00'
    #else:
        #print('Already Exists')
    
    

url = []
html = get_text()
parse_text(html)
print(len(url))
for i in range(1,len(url)):
    scd_url = url[i]
    print(i)
    print(scd_url)
    images_url = []
    html = get_page(scd_url)
    parse_page(html)
    for new_url in images_url:
        #print(str(new_url.split('/')[-1]))
        save_image(new_url)
    





