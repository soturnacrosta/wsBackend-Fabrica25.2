from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),  
    path('sincronizar/', views.SincronizarView.as_view(), name='sincronizar'),
    path('listar/', views.PostListView.as_view(), name='listar_posts'),
    path('criar/', views.PostCreateView.as_view(), name='criar_posts'),
    path('update/<int:post_id>/', views.PostUpdateView.as_view(), name='atualizar_posts'),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view(), name='deletar_posts'),

]