'use strict';

angular.
  module('core.news').
  factory('News', ['$resource',
    function($resource) {
      return $resource('news.json', {}, {
        query: {
          method: 'GET',
          params: '',
          isArray: false
        }
      });
    }
  ]);
