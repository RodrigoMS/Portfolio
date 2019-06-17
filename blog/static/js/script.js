function changePage(link) {
	var element = document.getElementsByTagName('body')[0];

    element.style.WebkitAnimation = "fadeOut 0.8s ease-in-out"; /* Safari */
    element.style.animation = "fadeOut 0.8s ease-in-out";
    
    setTimeout(function(){
    	window.location.href = link;
    },600);
}

function menuOpenClose() {
	var element = document.getElementsByTagName('aside')[0];

	if(element.style.display != "block") {

		element.style.display = "block";

	} else {
		var subElement = element.getElementsByTagName("div")[0];

		subElement.style.WebkitAnimation = "leftInput 0.4s ease-in-out";
		subElement.style.animation = "leftInput 0.4s ease-in-out";

	    element.style.WebkitAnimation = "fadeOut 0.4s ease-in-out";
	    element.style.animation = "fadeOut 0.4s ease-in-out";

	    setTimeout(function(){
			element.style.display = "none";
		},400);

		setTimeout(function(){
			subElement.style.WebkitAnimation = "rightInput 0.4s ease-in-out";
			subElement.style.animation = "rightInput 0.4s ease-in-out";

			element.style.WebkitAnimation = "fadeIn 0.4s ease-in-out";
	    	element.style.animation = "fadeIn 0.4s ease-in-out";
		}, 600);
	}
}

function rotateZoom(element, color, link) {
	element.style.WebkitAnimation = "rotateZoom 1.5s ease-in-out";
	element.style.animation = "rotateZoom 1.5s ease-in-out";
	element.style.zIndex = "4";

	setTimeout(function(){
		element.getElementsByTagName('img')[0].style.opacity = "0";
		element.style.backgroundColor = color;
	},410);

	setTimeout(function(){
    	window.location.href = link;
    },1450);
}