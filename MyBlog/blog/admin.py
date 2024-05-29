from django.contrib import admin
from .models import Post, Author, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Comment)
