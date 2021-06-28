from django.urls.conf import path
from livros import views

urlpatterns = [
    path('', views.index, name='home'),
    path('livros/<int:livro_id>/', views.detalhes, name='detalhes'),
    path('livros/cadastrar', views.cadastrar, name='cadastrar'),
    path('livros/editar/<int:livro_id>/', views.editar, name='editar'),
    path('livros/excluit<int:livro_id>/', views.excluir, name='excluir')
]