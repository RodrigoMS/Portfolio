function carregarProdutos(){

	var produto = [
		'PEDIVELA SHIMANO TOURNEY FC-TY501 42-34-24D 6 7 E 8V',
		'ABRAÇADEIRA CONTROLTECH COM BLOCAGEM PRETA',
		'CÂMBIO TRASEIRO SRAM NX PRETO LONG CAGE 11 VELOCIDADES',
		'CASSETE SRAM GX PRETO 11V 10-42 DENTES MTB XG-1150',
		'MOVIMENTO CENTRAL SRAM PRESSFIT GXP MTB BB92 24MM',
		'TROCADOR DE MARCHA SRAM NX TRIGGER TRASEIRO 11V',
		'CORRENTE BIKE SRAM 11V PC 1110',
		'ENGRENAGEM PARA PEDIVELA SRAM GX EAGLE 3MM OFFSET 32 DENTES (BOOST)',
		'MESA BIKE CONTROLTECH TUX 5° CARBONO',
		'PEDIVELA SHIMANO DEORE FC-M615 28-40D 10V HOLLOWTECH II',
		'EMENDA DE CORRENTE SRAM 10 VELOCIDADES',
		'PNEU BIKE VITTORIA MEZCAL TNT 29" X 2.25 MTB'
	];

	var preco = [
		'R$ 143,10',
		'R$ 82,80',
		'R$ 746,10',
		'R$ 1.003,50',
		'R$ 323,10',
		'R$ 269,10',
		'R$ 152,10',
		'R$ 301,50',
		'R$ 617,40',
		'R$ 675,59',
		'R$ 35,10',
		'R$ 332,09'
	];

	var local = document.getElementById('produtos');

	for (var i = 0; i < produto.length; ++i) {
		local.innerHTML += '<div><img src="/static/rmsbiker/_imagens/_produtos/prod' + i + '.jpg" class="produto" onclick="exibirProduto(this.src)"> <span>' + produto[i] + '</span><br><b>' + preco[i] + '</b></div>';
	}
		
}

function exibirProduto(local) {
	var imagem = document.getElementById("imagem");

	imagem.src = local;
	document.getElementById("tela").style.display = "block";
}

function fechar() {
	document.getElementById("tela").style.display = "none";
}
