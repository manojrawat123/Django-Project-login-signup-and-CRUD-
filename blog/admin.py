from django.contrib import admin
from blog.models import Blogpost
# Register your models here.
@admin.register(Blogpost)
class BlogAdminPost(admin.ModelAdmin):
    list_display = ["id", "title", "desc", "author"]