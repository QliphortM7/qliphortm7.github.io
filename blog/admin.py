from django.contrib import admin
from blog import models

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')


admin.site.register(models.Article, ArticleAdmin)
