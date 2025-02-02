from django.contrib import admin
from django.utils.html import format_html
from .models import Post, Comment, LikeDislike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_at', 'display_image')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<a target="_blank" href="{}"><img src="{}" height="50" /></a>', 
                obj.get_absolute_url(), 
                obj.image.url
            )
        return "No Image"
    display_image.short_description = 'Image'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'content', 'created_at')
    search_fields = ('content', 'user__username', 'post__title')
    list_filter = ('created_at', 'user')
    ordering = ('-created_at',)

@admin.register(LikeDislike)
class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_like')
    list_filter = ('is_like', 'post')
    search_fields = ('user__username', 'post__title')