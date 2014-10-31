#coding=utf-8
from bs4 import BeautifulSoup
import urllib2
import re
import string
#import html2text


'''
#兄弟结点遍历
def find(tag,content):
  if tag['class']!=content:
    find(tag.next_sibling,content)
  else:
    return tag  
'''


#转化为markdown格式
def markdown(tag):
  head=tag.h1.text.encode('utf-8')
  f=open(head+'.md','w')
  s='**'+str(head)+'**\n=\n---\n'
  
  s+=str(tag.find('div','article-info').encode('utf-8'))

  s+=str(tag.a.img)+'\n'
  s+=str('-'+tag.a.span.text.encode('utf-8'))+'\n\n---\n'

  for para in tag.find('div','show-content').find_all('p'):
    if para.text:
      s+=str('>'+para.text.encode('utf-8')+'\n\n')
  f.write(s)
'''  
  for li in tag.div.div.a.content:
    if str(li.name)=='div':
      s+=str(li.image)
    else:
      s+=str(li.text.encode('utf-8'))
''' 
   

#获取文章内容
def visit(url):
  soup=BeautifulSoup(urllib2.urlopen(url).read())
 # tag=soup.body
 #tag=tag.find("div",id="show-note-container")
 #tag=tag.div.find("div","container")
  tag=soup.find("div","preview")
 # print(tag.prettify)
 # print(tag['class']) 
  markdown(tag)

#查找100篇文章
def container(url):
  soup=BeautifulSoup(urllib2.urlopen(url).read())
  host='http://jianshu.com'
  for li in soup.find_all("li","span4",limit=3):
    url=host+li.a['href']
    print(url)
    visit(url)

#查找专题
def find_subject(url):
  soup=BeautifulSoup(urllib2.urlopen(url+'/collections').read())
  for li in soup.find_all("li","span4",limit=1):
    print(li.a.h4.string)
    url=url+li.a['href']
    print(url)
    container(url)

url='http://www.jianshu.com'
find_subject(url)
