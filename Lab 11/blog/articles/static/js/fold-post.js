var foldBtns = document.getElementsByClassName("fold-button");
for (var i = 0; i<foldBtns.length; i++)
{
    foldBtns[i].addEventListener("click", function(event) {
		if (this.innerHTML=="Свернуть")
		{
			this.parentElement.className='one-post folded';
			this.innerHTML="Развернуть";
		}
		else
		{
			this.parentElement.className='one-post';
			this.innerHTML="Свернуть";
		}
    });
	
	/*foldBtns[i].addEventListener("click", function(e) {
    if (e.target.className == "fold-button folded"){
        e.target.innerHTML = "Свернуть";
        e.target.className = "fold-button";
        var displayState = "block";
    }
    else{
        e.target.innerHTML = "Развернуть";
        e.target.className = "fold-button folded";
        var displayState = "none";
    }
    event.target
        .parentElement
        .getElementsByClassName('article-author')[0]
        .style.display = displayState;
    event.target
        .parentElement
        .getElementsByClassName('article-created-date')[0]
        .style.display = displayState;
    event.target
        .parentElement
        .getElementsByClassName('article-text')[0]
        .style.display = displayState;
	});*/
}