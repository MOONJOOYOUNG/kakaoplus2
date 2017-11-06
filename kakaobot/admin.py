from django.contrib import admin

# Register your models here.

import requests
from bs4 import BeautifulSoup
from collections import OrderedDict
from itertools import count

def naver_blog_search(q, max_page=None):
     post_dict = OrderedDict()

     for page in count(1):
         url = 'https://search.naver.com/search.naver'
         params = {
              'query': q,
              'where': 'post',
              'start': (page-1)*10 +1,
         }
         response = requests.get(url, params=params)
         html = response.text
         soup = BeautifulSoup(html, 'html.parser')

         print(response.request.url)

         for tag in soup.select('.sh_blog_title'):
             if tag['href'] in post_dict:
                 return post_dict
              post_dict[tag['href']] = tag.text
         if max_page and (page >= max_page):
              return post_dict