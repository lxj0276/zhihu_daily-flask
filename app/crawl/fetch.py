#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = ['"wuyadong" <wuyadong311521@gmail.com>']


import os
import httplib
import urlparse
import datetime
import logging
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


def yesterday_date_str(date_str):
    """计算前一天的date_str
    """
    now_date = datetime.datetime.strptime(date_str, "%Y%m%d")
    before_date = now_date - datetime.timedelta(days=1)
    return before_date.strftime("%Y%m%d")


def tomorrow_date_str(date_str):
    """计算后一天的date_str
    """
    now_date = datetime.datetime.strptime(date_str, "%Y%m%d")
    before_date = now_date + datetime.timedelta(days=1)
    return before_date.strftime("%Y%m%d")


def is_today_str(date_str):
    """判断是否是今天
    """
    if datetime.datetime.now().strftime("%Y%m%d") == date_str:
        return True
    else:
        return False


def today_str():
    """获取今天的日期
    """
    return datetime.datetime.now().strftime("%Y%m%d")


def extract_news_ids(latest_news):
    """提取出最新的news_ids
    """
    news_ids = []

    stories = latest_news['stories']
    for story in stories:
        news_ids.append(story['id'])

    return news_ids


def extract_date_str(latest_news):
    """提取出最新的日期
    """
    return latest_news['date']


#  def fetch_image(news_url, image_url):
    #  import urllib2
    #  img_name = image_url.split('/')[-1]

    #  req = urllib2.Request(image_url)
    #  req.add_header('Referer', news_url)
    #  data = urllib2.urlopen(req).read()

    #  img_temp = NamedTemporaryFile()
    #  img_temp.write(data)
    #  img_temp.flush()
    #  return img_name, File(img_temp)


def fetch_image(news_url, image_url, dir=None):
    """获取图片内容
    """
    _, host_port, path, _, _ = urlparse.urlsplit(image_url)
    host_port = host_port.split(":")
    host = host_port[0]
    port = int(host_port[1]) if len(host_port) > 1 else 80

    http = httplib.HTTPConnection(host, port, timeout=10)
    http.request("GET", path, headers={"Referer": news_url})
    response = http.getresponse()
    if response.status / 100 == 2:
        data = response.read()

        img_name = image_url.split('/')[-1]
        img_temp = NamedTemporaryFile()
        img_temp.write(data)
        img_temp.flush()
        logging.info('==> fetch image: ', img_name)
        print '==> fetch image: ', img_name
        if dir:
            if not os.path.exists(dir):
                os.makedirs(dir)
            file_path = os.path.join(dir, img_name)
            print '==> ', file_path
            with open(file_path, 'wb') as f:
                f.write(data)
                f.flush()
        return img_name, File(img_temp)
    else:
        return None, None
