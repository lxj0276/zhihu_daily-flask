$(document).ready(function(){

var app = new Vue({
    el: '#app',
    data: {
      news: null
    }
});
$.getJSON('/news/', function (data) {
    app.news = data.stories;
});

});
