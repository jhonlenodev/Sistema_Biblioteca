from django.urls.conf import path
from livros import views

urlpatterns = [
    path('', views.index, name='home'),
    path('livros/<int:livro_id>/', views.detalhes, name='detalhes')
]