from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import *

# --------------------------------------------------------- #
# --------------------- Link do blog ---------------------- #
# --------------------------------------------------------- #
from django.shortcuts import get_object_or_404
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# --------------------------------------------------------- #
# ----------------------- Portfolio ----------------------- #
# --------------------------------------------------------- #
#renderiza o arquivo inicio.html
def portifolio_inicio(request):
    habilidades = Habilidade.objects.all()
    projetos = Projeto.objects.all()
    contato = Contato.objects.filter(id = "1")
    return render(request, 'blog/inicio.html',{'habilidades': habilidades, 'projetos': projetos, 'contatos': contato})

#def portifolio_blog(request):
    #return render(request, 'blog/blog.html',{})

def portifolio_blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/blog.html', {'posts': posts})

def portifolio_biografia(request):
    biografia = Biografia.objects.filter(id = "1")
    formacaos = Formacao.objects.order_by('-id')
    profissaos = Profissao.objects.order_by('-id')
    return render(request, 'blog/biografia.html',{'biografia': biografia, 'formacaos': formacaos, 'profissaos': profissaos})

#def portifolio_biografia(request):
    #return render(request, 'blog/biografia.html',{})

def portifolio_contato(request):
    contato = Contato.objects.filter(id = "1")
    return render(request, 'blog/contato.html',{'contatos': contato})

#def portifolio_contato(request):
    #return render(request, 'blog/contato.html',{})

# --------------------------------------------------------- #
# ------------------ Template RMSbiker -------------------- #
# --------------------------------------------------------- #
#renderiza os arquivos da pasta rmsbiker
def rmsbiker_index(request):
    return render(request, 'blog/rmsbiker/index.html',{})

def rmsbiker_sobre_nos(request):
    return render(request, 'blog/rmsbiker/sobre_nos.html',{})

def rmsbiker_produtos(request):
    return render(request, 'blog/rmsbiker/produtos.html',{})

def rmsbiker_servicos(request):
    return render(request, 'blog/rmsbiker/servicos.html',{})

def rmsbiker_contato(request):
    return render(request, 'blog/rmsbiker/contato.html',{})

# --------------------------------------------------------- #
# --------------- Template w3_css_youtube ----------------- #
# --------------------------------------------------------- #
#renderiza os arquivos da pasta w3_css_youtube
def w3_css_youtube_index(request):
    return render(request, 'blog/w3_css_youtube/index.html',{})

