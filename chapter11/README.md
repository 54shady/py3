# Web Scraping

## 安装必要模块

sudo pip install beautifulsoup4

## 代码流程简要分析

- 使用requests模块来下载网页

- 使用BeautifulSoup 找到图片的URL

- 使用iter_content将文件写入硬盘

- 找到Previous按钮的连接,重复上面的操作
