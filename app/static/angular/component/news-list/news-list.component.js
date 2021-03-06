'use strict';

angular.
  module('newsList').
  component('newsList', {
    templateUrl: '/static/angular/component/news-list/news-list.template.html',
    controller: ['$routeParams', 'News',
      function NewsListController($routeParams, News) {
        var now = new Date()
        var date_params = $routeParams.date
        if (date_params && date_params.length === 8){
          var date_str = date_params.substring(0,4) + '/' + date_params.substring(4,6) + '/' + date_params.substring(6)
          var date = new Date(date_str)
          if(date.addDays(1) < now)
            this.next = date.addDays(1).formateDate()
          this.previous = date.addDays(-1).formateDate()
        } else {
          this.previous = (new Date()).addDays(-1).formateDate()
        }

        // this.news = chunk(News.get({date: date_params}).stories, row);
        var self = this
        var data = News.get({date: date_params}, function(){
          var row = 3
          self.news = chunk(data.stories, row)
          // console.log('==> ', self.news)
        })

        this.search = function() {
          console.log('==> search submit')
        }

      }
    ]
  });
