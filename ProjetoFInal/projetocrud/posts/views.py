from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Users
import requests

API_URL_POSTS = "https://jsonplaceholder.typicode.com/posts/"
API_URL_USERS = "https://jsonplaceholder.typicode.com/users/"


class HomeView(TemplateView):

    template_name = 'home.html'

class SincronizarView(View):

    def get(self, request, *args, **kwargs):

        users_response = requests.get(API_URL_USERS)
        users_data = users_response.json()
        for user_item in users_data:
            Users.objects.get_or_create(
                api_id=user_item['id'],
                defaults={
                    'name': user_item['name'],
                    'username': user_item['username'],
                    'email': user_item['email']
                }
            )
        
        posts_response = requests.get(API_URL_POSTS)
        posts_data = posts_response.json()

        for post_item in posts_data:

            try:
                
                user = Users.objects.get(api_id=post_item['userId'])
                Post.objects.get_or_create(
                    api_id=post_item['id'],

                    defaults={

                        'title': post_item['title'],
                        'body': post_item['body'],
                        'user': user

                    }

                )

            except Users.DoesNotExist:

                continue
        
        return redirect('listar_posts')


class PostListView(ListView):

    model = Post
    template_name = 'listar_posts.html'
    context_object_name = 'posts'


class PostCreateView(CreateView):

    model = Post
    template_name = 'criar_posts.html' # tem que ter o nome correto dos templates!!!
    fields = ['title', 'body']
    success_url = reverse_lazy('listar_posts')

    def form_valid(self, form):

        form.instance.user = Users.objects.first()
        return super().form_valid(form)

class PostUpdateView(UpdateView):

    model = Post
    template_name = 'atualizar_posts.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('listar_posts')

class PostDeleteView(DeleteView):

    model = Post
    template_name = 'deletar_posts.html' 
    success_url = reverse_lazy('listar_posts')