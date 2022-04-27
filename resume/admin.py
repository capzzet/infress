from django.contrib import admin
from .models import *
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links = ('id','title')
    list_editable = ('is_published',)
    search_fields = ('title','time_create')
    list_filter = ('is_published','time_create')
    prepopulated_fields = {'slug':('title',)}
admin.site.register(Blog,BlogAdmin)