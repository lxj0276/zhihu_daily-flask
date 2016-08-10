#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import render_template, request
from flask import abort
from flask import session, redirect, url_for, current_app

from . import main
from .. import db
from ..models import News
from ..crawl.fetch import today_str, yesterday_date_str, tomorrow_date_str


@main.route('/', methods=['GET', 'POST'])
def index():
    news_list = News.query.all()
    date_str = request.args.get("date", today_str())
    before_date = yesterday_date_str(date_str)
    after_date = tomorrow_date_str(date_str) \
        if today_str() != date_str else None

    return render_template(
        'index.html',
        news_list   = news_list,
        before_date = before_date,
        after_date  = after_date
    )


from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def page_range(self):
        return range(1, self.pages + 1)

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def previous_page_number(self):
        if self.has_prev:
            return self.page - 1

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def next_page_number(self):
        if self.has_next:
            return self.page + 1

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in range(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


@main.route('/search/', methods=['GET', 'POST'])
def search():
    page_size = 2
    page = int(request.args.get('page', 1))
    keyword = request.args.get('keyword', '')

    if not keyword.strip():
        return redirect('/')

    result = News.query.filter(News.title.contains(keyword))
    count = result.count()
    if not result and page != 1:
        abort(404)
    pagination = Pagination(page, page_size, count)
    return render_template(
        'search.html',
        page       = page,
        pagination = pagination,
        keyword    = keyword,
        result     = result[(page - 1) * page_size: page * page_size],
    )


