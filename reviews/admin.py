from django.contrib import admin
from .models import Review, Comment

# Register your models here.
# https://docs.djangoproject.com/en/3.2/intro/tutorial07/
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ('title', 'created_at', 'updated_at')

class CommentAdmin(admin.ModelAdmin):
    list_display  = ('content', 'created_at', 'review')

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)