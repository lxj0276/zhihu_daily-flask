'use strict';

Date.prototype.addDays = function(days) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + days);
  return date;
}

Date.prototype.formateDate = function() {
  var mm = this.getMonth() + 1;
  var dd = this.getDate();
  return [this.getFullYear(), !mm[1] && '0', mm, !dd[1] && '0', dd].join('');
};

function chunk(arr, size) {
  // console.log('==> arr: ', arr)
  var newArr = [];
  for (var i=0; i<arr.length; i+=size) {
    newArr.push(arr.slice(i, i+size));
  }
  return newArr;
}
