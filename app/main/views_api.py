#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request
from flask import url_for
from flask_restful import Resource

from ..models import News
from . import main
from . import api


class NewsAPI(Resource):
    def get(self):
        search_title = request.args.get("title")

        news = None
        if search_title:
            news = News.query.filter(News.title.contains(search_title))
        else:
            news = News.query.all()

        resp = {
            'status': 0,
            'stories': []
        }
        for i in news:
            resp['stories'].append({
                'id'         : i.news_id,
                'date'       : i.date,
                'title'      : i.title,
                'share_url'  : i.share_url,
                'image_file' : url_for('static', filename='image/' + i.date + '/' + i.image_file),
                'image_name' : i.image_name,
            })
        return resp

api.add_resource(NewsAPI, '/news/')
