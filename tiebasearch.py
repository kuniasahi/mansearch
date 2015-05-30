#!/usr/bin/env python

import re
import os
import sys
import time
import random
import urllib


def get_urls_in_apage(page):
   out = re.findall(r'href\=\"\/p\/[^\s]*',page)
   for i in out:
      #print i
      t = "http://tieba.baidu.com" + i[6:len(i)-1]
      print t
      cid = re.findall(r'\#[^\s]*',t)
      ids = cid[0][1:]
      #print ids

   

def get_record_size(tname):
   urls = "http://tieba.baidu.com/f/search/ures?ie=utf-8&kw=&qw=&rn=30&un="
   req = urllib.urlopen(urlstr + tname)
   web = req.read()
   totalsizestr = re.findall(r's\_nav\_right hasPage[^\s]*',web)
   totalsize = re.findall(r'[0-9][0-9]{0,}',totalsizestr[0])
   sizex = int(totalsize[0])
   return sizex

if __name__ == '__main__':
   urlstr = "http://tieba.baidu.com/f/search/ures?ie=utf-8&kw=&qw=&rn=30&un="
   if(len(sys.argv)==3 and sys.argv[1] == '-k' ):
       namex = sys.argv[2]
       sizex = get_record_size(namex)
       print "find all record size = " + str(sizex)
       rn = 30
       pn = sizex / rn
       print pn
       i = 1
       while i < pn:
          newurl = urlstr + namex +"&" + "pn=" + str(i)
          print newurl
          reqx = urllib.urlopen(newurl)
          web2 = reqx.read()
          get_urls_in_apage(web2)
          i = i + 1
          if i > 76:
             break
          print str(i)
          time.sleep(1)
