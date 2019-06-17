var i = 1;

setInterval(function(){
	if(i == 7) {
		document.getElementById('imagem6').remove();
		i = 0;
	}else {
		document.getElementById('imagem'+(i-1)).remove();
	}

document.getElementById('oficina').innerHTML += '<img id="imagem'+ i +'" class="centro" src="/static/rmsbiker/_imagens/oficina'+ i +'.jpg"/>';

	++i;			

}, 4000);