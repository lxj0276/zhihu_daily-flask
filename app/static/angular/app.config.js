'use strict';

angular.
  module('zhihuDaily').
  config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
      $locationProvider.hashPrefix('!');
      $routeProvider.
        when('/', {
          // template: '<h1>hello</h1>'
          template: '<news-list></news-list>'
        }).
        when('/search', {
          template: '<news-search></news-search>'
        }).
        when('/news', {
          template: '<news-list></news-list>'
        }).
        otherwise('/news');
    }
  ]);



