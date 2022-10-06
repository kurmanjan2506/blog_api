from django.contrib import admin
from .models import Post, Category, Comment


admin.site.register(Post)
admin.site.register(Category)


@admin.register(Comment)
class Comm(admin.ModelAdmin):
    list_display = ('owner', 'post', 'body', 'created_at')