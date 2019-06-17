
function trocaPagina(link) {
    document.getElementById("interface").style.WebkitAnimation = "fadeOut 1s ease-in-out"; /* Safari */
    document.getElementById("interface").style.animation = "fadeOut 1s ease-in-out";
    
    setTimeout(function(){
    	window.location.href = link;
    },900);
}