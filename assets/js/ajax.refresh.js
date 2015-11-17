setInterval(function(){
            $.ajax({
               url: /requests/,
               success: function(data) {
                  var html = $(data).filter('#refresh').html();
                  $('#refresh').html(html);
                  //var myTitle = $(data).filter('title').html();
                  //$('title').html(myTitle);
                  }
            });
        }, 2000);