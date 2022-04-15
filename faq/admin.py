from django.contrib import admin
from .models import FaqPosts, CommentsFaqPost


class FaqPostsAdmin(admin.ModelAdmin):
    list_display = (
        'date_added',
        'author',
        'question',
        'answer',
        'author',
    )

    search_fields = ('author', 'question')


class CommentsFaqPostAdmin(admin.ModelAdmin):
    list_display = (
        'date_added',
        'comments_author',
        'comment',
        'text',
    )


admin.site.register(FaqPosts, FaqPostsAdmin)
admin.site.register(CommentsFaqPost, CommentsFaqPostAdmin)
