$(document).ready(function() {
   setInterval(function(){
      $.ajax({
         url: '/requests/',
         success: function(data) {
            $('#refresh').html($(data).filter('#refresh').html());
            $('title').html($(data).filter('title').html());
         }
      });
   }, 2000);
});
