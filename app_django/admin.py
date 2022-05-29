from django.contrib import admin
from . import models


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """
    Настройки отображения, фильтрации и поиска модели:'Post' на панели администратора
    """

    list_display = (
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    )
    list_display_links = (
        'title',
        'description',
    )
    list_editable = (
        'is_completed',
    )
    list_filter = (
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    )
    fieldsets = (
        ('Основное', {'fields': (
            'title',
            'description',
            'is_completed',
            'created',
            'updated'
        )}),
    )
    search_fields = [
        'title',
        'description',
        'is_completed',
        'created',
        'updated'
    ]


admin.site.register(models.Post, PostAdmin)
