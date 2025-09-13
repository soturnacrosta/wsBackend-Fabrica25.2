from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),  
    path('sincronizar/', views.SincronizarView.as_view(), name='sincronizar'),
    path('listar/', views.PostListView.as_view(), name='listar_posts'),
    path('create/', views.PostCreateView.as_view(), name='create_post'),
    path('update/<int:post_id>/', views.PostUpdateView.as_view(), name='update_post'),
    path('delete/<int:post_id>/', views.PostDeleteView.as_view(), name='delete_post'),

]