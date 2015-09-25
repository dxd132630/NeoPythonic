# -*- coding: utf-8 -*- 

import requests

import re

import urlparse

email_re = re.compile(r'([\w\.,]+@[\w\.,]+\.\w+)')

link_re = re.compile(r'href=".*?"')


def crawl(url, maxlevel):


    if(maxlevel == 0):

        return

    req = requests.get(url)

    result = []

    if(req.status_code != 200):

        return []


    links = link_re.findall(req.text)

    for link in links:

        link = urlparse.urljoin(url, link)

        result += crawl(link, maxlevel - 1)

    result += email_re.findall(req.text)

    return result

emails = crawl('https://github.com/dxd132630', 2)

print "Scrapped e-mail addresses:"

for e in emails:

    print e
