$(document).ready(function(){
    $('.one-post').hover(function(event){
        /*console.log("Навели");
		console.log(event.currentTarget);*/
		$(event.currentTarget).find('.one-post-shadow').animate({opacity:
'0.2'}, 300);
    }, function(event){
        /*console.log("Вывели");*/
		$(event.currentTarget).find('.one-post-shadow').animate({opacity: '0'}, 
300);
    });
	$('.main').hover(function(event){
		var NewWidth=parseInt($(this).css('width').replace('px',''))+50+'px';
		$(this).animate({width:NewWidth},300);
	},function(event){
		var NewWidth=parseInt($(this).css('width').replace('px',''))-50+'px';
		$(this).animate({width:NewWidth},300);
	})
});
