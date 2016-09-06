'use strict';

angular.
  module('newsList').
  component('newsList', {
    templateUrl: 'news-list/news-list.template.html',
    controller: ['News',
      function NewsListController(News) {
        this.news = News.query();
      }
    ]
  });
