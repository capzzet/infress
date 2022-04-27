from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from docxtpl import DocxTemplate
from .models import *
import os
import mimetypes
from docx2pdf import convert
from pathlib import Path


# Create your views here.
def index(request):
    context = {
        'intro_under': [{'data_scroll': '#about', 'under_text': 'Что такое конструктор', },
                        {'data_scroll': '#benefits', 'under_text': 'Преимущества', },
                        {'data_scroll': '#creation', 'under_text': 'Процесс создания', },
                        {'data_scroll': '#footer', 'under_text': 'Связаться', }, ],
    }
    return render(request, 'resume/html/index.html', context=context)


def about(request):
    return render(request, 'resume/html/about.html')


def blog(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'resume/html/blog.html', context=context)


def show_blog(request, blog_slug):
    blog = get_object_or_404(Blog,slug=blog_slug)
    context=  {
        'blog':blog,
        'title':blog.title
    }
    return render(request,'resume/html/blog_id.html',context=context)


def contacts(request):
    return render(request, 'resume/html/contacts.html')




def custom_page_not_found_view(request, exception):
    return render(request, "resume/errors/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "resume/errors/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "resume/errors/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "resume/errors/400.html", {})
