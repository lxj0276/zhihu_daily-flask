'use strict';

angular.
  module('newsSearch').
  component('newsSearch', {
    templateUrl: '<h2>news search</h2>',
    controller: ['News',
      function NewsSearchController(News) {
        this.news = News.query();
      }
    ]
  });
