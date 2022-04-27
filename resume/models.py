from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=255,verbose_name='Название статьи')
    slug = models.SlugField(max_length=255,unique=True,db_index=True,verbose_name='URL')
    content = models.TextField(verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/',verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    is_published = models.BooleanField(default=True,verbose_name='Опубликовано')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog_name',kwargs={'blog_slug':self.slug})
    #     resumeroot
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering =  ['-time_create','title']