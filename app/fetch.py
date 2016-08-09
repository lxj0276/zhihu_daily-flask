#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import os

from flask import current_app as app
from flask_script import Command

from .models import News
from . import db
from crawl import zhihu
from crawl import fetch


class Fetch(Command):
    def run(self):
        image_folder = os.path.join(app.static_folder, 'image')

        zh = zhihu.ZhiHu()
        latest_news = zh.get_latest_news()

        latest_news_ids = fetch.extract_news_ids(latest_news)
        date_str = fetch.extract_date_str(latest_news)

        for id in latest_news_ids:
            if News.query.filter_by(news_id=id).first():
                continue
            news = zh.get_news(id)
            file_folder = os.path.join(image_folder, date_str)
            image_file, _ = fetch.fetch_image(news['share_url'], news['image'], dir=file_folder)
            print '==> title', news['title']
            data = News(
                news_id=id,
                date=date_str,
                title=news['title'],
                share_url=news['share_url'],
                image_name=news['image_source'],
                image_file=image_file,
            )
            db.session.add(data)
        db.session.commit()


