# -*- coding:utf-8 -*-
import os
import urllib.request
from bs4 import BeautifulSoup

urls = set() # 存放需要爬取的URL集合
res_data = [] # 存放需要爬取的图片的URL

# 获得要爬取的范围
print('请输入要爬取的页面范围\n例：输入1 2，则爬取第1页和第2页的图片')
print('请输入首页')
front_page = input()
print('请输入尾页')
back_page = input()

# 获取需要爬取的URL
if front_page == back_page:
    url = 'http://baozoumanhua.com/catalogs/gif?page=' + front_page
    urls.add(url)
else:
    for i in range(int(front_page), int(back_page)+1):
        url = 'http://baozoumanhua.com/catalogs/gif?page=' + str(i)
        urls.add(url)

# 模拟浏览器
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
headers = {'User-Agent': user_agent}

# 从URL集合中，取出一个URL进行解析
for url in urls:
    req = urllib.request.Request(url, headers=headers) # 请求页面
    response = urllib.request.urlopen(req) # 下载页面
    html = response.read().decode('utf-8') # 编码格式化为UTF-8

    # 解析页面
    soup = BeautifulSoup(html, 'html.parser')
    gif1s = soup.findAll('video', style='width: 500px; height: 500px;')
    gif2s = soup.findAll('img', class_='lazy')
    res_data += [gif['data-original-image-url']for gif in gif1s]
    res_data += [gif['data-original-image-url']for gif in gif2s]

# 在当前目录下，建立存储gif图片的文件夹
if not os.path.exists('./download_gif'):
    os.mkdir('download_gif')

# 下载图片
for i in range(len(res_data)):
    filename = str(i) + ".gif"
    urllib.request.urlretrieve(res_data[i], './download_gif/' + filename)
