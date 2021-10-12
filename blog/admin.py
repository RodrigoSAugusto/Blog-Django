from django.contrib import admin
from django.contrib.admin.options import ModelAdmin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}