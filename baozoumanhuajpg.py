# -*- coding:utf-8 -*-
import os
import urllib.request
from bs4 import BeautifulSoup

urls = set() # 存放需要爬取URL集合
res_data = [] # 存放需要爬取图片的URL集合

# 获得要爬取的范围
print('请输入要爬取的页面范围\n例：输入1 2，则爬取第1页和第2页的图片')
print('请输入首页')
front_page = input()
print('请输入尾页')
back_page = input()

# 获得URL
if front_page == back_page:
    url = 'http://baozoumanhua.com/catalogs/jpg?page=' + front_page
    urls.add(url)
else:
    for i in range(int(front_page), int(back_page)+1):
        url = 'http://baozoumanhua.com/catalogs/jpg?page=' + str(i)
        urls.add(url)

# 模拟浏览器
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
headers = {'User-Agent': user_agent}

# 从带爬取的URL集合中，取出一个URL
for url in urls:
    req = urllib.request.Request(url, headers=headers) # 请求页面
    response = urllib.request.urlopen(req) # 下载页面
    html = response.read().decode('utf-8')  # 代码格式UTF-8

    # 解析网页
    soup = BeautifulSoup(html, 'html.parser')
    imgs = soup.findAll('img', class_="lazy")
    res_data += [img['data-original']for img in imgs]

# 为当前目录建立个文件夹，用于储存图片
if not os.path.exists('./download_jpg/'):
    os.mkdir('download_jpg')

# 下载图片，并保存到download_jpg 文件夹中
for i in range(len(res_data)):
    filename = str(i) + ".jpg"
    urllib.request.urlretrieve(res_data[i], './download_jpg/' + filename)  # 下载图片内容
