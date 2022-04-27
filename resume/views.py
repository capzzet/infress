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


def resume(request):
    if request.method == 'POST':
        doc = DocxTemplate(rf'{Path(__file__).resolve().parent.parent}/resume/templates_docx/blank-rezume-{request.POST["doc_template"]}.docx')
        context = {'Surname': request.POST['Surname'],'name': request.POST['name'],'patronymic': request.POST['patronymic'],
                   'position': request.POST['position'],'wage': request.POST['wage'],'employment': request.POST['employment'],
                   'schedule': request.POST['schedule'],'telephone': request.POST['telephone'],'mail': request.POST['mail'],
                   'city': request.POST['city'],'birthday': request.POST['birthday'],'sex': request.POST['sex'],
                   'Family': request.POST['Family'],'job_start': request.POST['job_start'],'job_end': request.POST['job_end'],
                   'job_Position': request.POST['job_Position'],'Organization': request.POST['Organization'],'job_responsibilities': request.POST['job_responsibilities'],
                   'educational_institution': request.POST['educational_institution'],'Faculty': request.POST['Faculty'],'Speciality': request.POST['Speciality'],
                   'Year_of_ending': request.POST['Year_of_ending'],'Form_of_study': request.POST['Form_of_study'],'lang': request.POST['lang'],
                   'attainments': request.POST['attainments'],'Recommendations': request.POST['Recommendations'],'Hobby': request.POST['Hobby'],
                   'Personal_qualities': request.POST['Personal_qualities'],'Year_of_start': request.POST['Year_of_start'],'experience': request.POST['experience']}
        doc.render(context)
        doc.save('resume.docx')
        filename = 'resume.pdf'
        filepath = rf'{Path(__file__).resolve().parent.parent}\resume.pdf'
        with open(filepath, 'rb') as path:
            mime_type, _ = mimetypes.guess_type(filepath)
            response = HttpResponse(path, content_type=mime_type)
            response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response
    return render(request, 'resume/html/resume.html')

def custom_page_not_found_view(request, exception):
    return render(request, "resume/errors/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "resume/errors/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "resume/errors/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "resume/errors/400.html", {})
