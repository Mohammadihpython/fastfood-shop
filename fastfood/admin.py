from django.contrib import admin
from django.contrib.admin import register

from fastfood.models import Foods, Category


@register(Foods)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'description', 'price', 'available', 'discount'
                    , 'published', 'modified_time', 'image', 'total_price',
                    'likes', 'like_count'
                    )
    search_fields = ('name', 'category')
    list_filter = ('name', 'category', 'available')


@register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)
