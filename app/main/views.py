#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from flask import render_template, request
from flask import session, redirect, url_for, current_app
from .. import db
from ..models import News
from . import main
from ..crawl.fetch import today_str, yesterday_date_str, tomorrow_date_str



#  @main.route('/', methods=['GET', 'POST'])
#  def index():
    #  form = NameForm()
    #  if form.validate_on_submit():
        #  user = User.query.filter_by(username=form.name.data).first()
        #  if user is None:
            #  user = User(username=form.name.data)
            #  db.session.add(user)
            #  session['known'] = False
            #  if current_app.config['FLASKY_ADMIN']:
                #  send_email(current_app.config['FLASKY_ADMIN'], 'New User',
                           #  'mail/new_user', user=user)
        #  else:
            #  session['known'] = True
        #  session['name'] = form.name.data
        #  return redirect(url_for('.index'))
    #  return render_template('index.html',
                           #  form=form, name=session.get('name'),
                           #  known=session.get('known', False))


@main.route('/', methods=['GET', 'POST'])
def index():
    #  news = News.query.all()

    #  resp = {
        #  'status': 0,
        #  'stories': []
    #  }
    #  for i in news:
        #  resp['stories'].append({
            #  'date'  : i.date,
            #  'title' : i.title,
            #  'image_file' : i.image_file
        #  })
    #  return json.dumps(resp)

    context = {}
    news_list = News.query.all()

    date_str = request.args.get("date", today_str())
    before_date = yesterday_date_str(date_str)
    after_date = tomorrow_date_str(date_str) \
        if today_str() != date_str else None


    return render_template(
        'index.html',
        news_list = news_list,
        before_date = before_date,
        after_date = after_date
    )



@main.route('/search', methods=['GET', 'POST'])
def search():
    return 'search view'

