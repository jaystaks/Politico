jQuery(document).ready(function($){
  $('.wiggle-bug .bug').hover(function(){
    $(this).addClass('animated infinite tada');
  }, function(){
    $(this).removeClass('animated infinite tada');
  });

  $('.wiggle-bug').click(function(){
    $(this).find('.bug').toggle('explode');
  });
});
