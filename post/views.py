from django.shortcuts import render
from .forms import PostForm
from .models import MyModel
from django.views.generic import ListView, TemplateView


class PostViews(ListView):
    model = MyModel
    template_name = 'post.html'


