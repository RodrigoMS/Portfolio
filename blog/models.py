from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

# Criando a tabela e elementos do blog.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    #text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    # Botao de publicação do post dentro do admin.
    # 127.0.0.1:8000/admin.
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # Exibição do título dento do admin.
    def __str__(self):
        return self.title

# Criando a tabela e elementos da habilidades.
class Habilidade(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Criando a tabela e elementos dos projetos do portifolio.
class Projeto(models.Model):
    title = models.CharField(max_length=50)
    link = models.CharField(max_length=200)
    image = models.ImageField(upload_to='../static/imagens')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Criando a tabela do texto inicial da Biografia.
#class Biografia(models.Model):
class Biografia(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Criando a tabela e elementos da formação escolar e cursos.
class Formacao(models.Model):
    title = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    text = models.TextField()
    local = models.CharField(max_length=100)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Criando a tabela e elementos das experiencias proficionais.
class Profissao(models.Model):
    title = models.CharField(max_length=50)
    period = models.CharField(max_length=50)
    text = models.TextField()
    local = models.CharField(max_length=100)


    def publish(self):
        self.save()

    def __str__(self):
        return self.title

# Criando a tabela e elementos dos dados de contato.
class Contato(models.Model):
    name = models.CharField(max_length=50)
    telephone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    country = models.CharField(max_length=20)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name