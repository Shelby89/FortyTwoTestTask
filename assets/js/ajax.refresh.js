$(document).ready(function() {
   setInterval(function(){
      $.ajax({
         url: '/requests/',
         success: function(data) {
            //var html = $(data).filter('#refresh').html();
            $('#refresh').html($(data).filter('#refresh').html());
            //var myTitle = $(data).filter('title').html();
            //$('title').html(myTitle);
            $('title').html($(data).filter('title').html());
         }
      });
   }, 2000);
});
