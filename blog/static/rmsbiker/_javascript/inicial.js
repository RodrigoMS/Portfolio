
// Carrega os vídeos.
function carregar() {
	player("video1", "https://www.youtube.com/embed/M1DKv133Hck");
	player("video2", "https://www.youtube.com/embed/QTtalrEfYk0");
	player("video3", "https://www.youtube.com/embed/P12Nr_1fjmE");
	player("video4", "https://www.youtube.com/embed/RfigtGKKVps");
}

// Cria o iframe que exibe os videos do YouTube.
function player(local, endereco) {
	document.getElementById(local).innerHTML = "";

	var largura = document.getElementById("contRelacionado").offsetWidth;
	largura = largura - 30;
	var altura = (290/510)*largura;

	var x = document.createElement("iframe");
	x.src = endereco;
	x.scrolling = "no";
	x.style.border = "none";
	x.setAttribute('allowFullScreen', '');

	document.body.appendChild(x).height=altura;
	document.body.appendChild(x).width=largura;
	document.getElementById(local).appendChild(x);
}