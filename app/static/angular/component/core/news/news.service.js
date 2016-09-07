'use strict';

angular.
  module('core.news').
  factory('News', ['$resource',
    function($resource) {
      return $resource('/daily/api/', {}, {
        get: {
          method: 'GET',
          params: '',
          // params: {"title": "为什么"},
          isArray: false
        }
      });
    }
  ]);
