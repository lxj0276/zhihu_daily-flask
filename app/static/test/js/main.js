$(document).ready(function(){
  var app = new Vue({
    config:{
      devtools: true,
      debug: true
    },
    el: '#app',
    data: {
      news: null,
      message: 'Hello Vue.js!'
    },
    ready: function () {
      $.ajax({
        url: "/news/",
        dataType: "json",
        success: function(data){
            app.news = data.stories;
        },
        error: function(data){
            console.log("==> read news fail");
        }
      });
    },
    methods: {
      reverseMessage: function () {
        this.message = this.message.split('').reverse().join('')
      },
      searchNews: function () {
        var keyword = this.keyword.trim()
        console.log('==> ' + keyword)
        $.ajax({
          url: "/news/?title=" + keyword,
          dataType: "json",
          success: function(data){
              app.news = data.stories;
              app.date = data.date;
          },
          error: function(data){
              console.log("==> serch news fail");
          }
        });
      }
    }
  });
});
