from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

from django.urls.conf import include

urlpatterns = [
	# --------------------------------------------------------- #
	# ---------------- Páginas do portifolio ------------------ #
	# --------------------------------------------------------- #

    path('', views.portifolio_inicio, name='inicio'),
    path('blog', views.portifolio_blog, name='blog'),
    path('biografia', views.portifolio_biografia, name='biografia'),
    path('contato', views.portifolio_contato, name='contato'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # --------------------------------------------------------- #
	# ------------------ Template RMSbiker -------------------- #
	# --------------------------------------------------------- #

    path('rmsbiker/', views.rmsbiker_index, name='index'),
    path('rmsbiker/sobre_nos/', views.rmsbiker_sobre_nos, name='sobre_nos'),
    path('rmsbiker/produtos/', views.rmsbiker_produtos, name='produtos'),
    path('rmsbiker/servicos/', views.rmsbiker_servicos, name='servicos'),
    path('rmsbiker/contato/', views.rmsbiker_contato, name='contato'),

    # --------------------------------------------------------- #
	# --------------- Template w3_css_youtube ----------------- #
	# --------------------------------------------------------- #

    path('w3_css_youtube/', views.w3_css_youtube_index, name='index'),

    # --------------------------------------------------------- #
    # --------------- Definição dos uploaders ----------------- #
    # --------------------------------------------------------- #

    path('ckeditor/', include('ckeditor_uploader.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
