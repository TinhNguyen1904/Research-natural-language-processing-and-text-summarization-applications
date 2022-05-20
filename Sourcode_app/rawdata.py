# -*- coding: utf-8 -*-
"""RawData.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wg0cLKnp8Qg9tELth4LeknhMItXWC-Qj
"""

#import thư viện
import bs4 as bs
import urllib.request
import re

#lấy link trang web
scraped_data = urllib.request.urlopen('https://baocantho.com.vn/sang-tao-do-bao-ho-giup-ha-nhiet-cho-cac-y-bac-si-a133867.html')
article = scraped_data.read()

article

#lấy tất cả thẻ p và xóa các html, các chú thích thẻ html
parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text

article_text

#Lưu file txt, tên file tùy chọn
f = open('demo_file2.txt', 'w')
f.write(article_text)

#đọc lại file xem đã lưu được dữ liệu chưa
f = open('demo_file2.txt', 'r')

str = f.read()

print ('Noi dung file cua ban la:\n', str)