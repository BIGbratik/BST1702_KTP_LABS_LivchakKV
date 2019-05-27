$(document).ready(function()
{
	var scrolled=0;
	var $parallaxElements=$('.paralaks img');
	var $Logo=$('.main');
	var yPos;
	var yLogoPos;
	$(window).scroll(function()
	{
		scrolled=$(window).scrollTop();
		for (var i=0;i<$parallaxElements.length;i++)
		{
			yPos=(scrolled*1*(i+1));
			$parallaxElements.eq(i).css({top:yPos});
		}
		/*for (var j=0;j<$Logo.length;j++)
		{
			yLogoPos=(scrolled*1*(i+1));
			$Logo.eq(i).css({top:yLogoPos});
		}*/
	});
});