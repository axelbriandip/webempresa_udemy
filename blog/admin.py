from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories') # Qué mostrar
    ordering = ('author', 'published') # ordenar en este orden..
    search_fields = ('title', 'author__username') # buscador: que busque en..
    date_hierarchy = 'published' # que me separando según..
    list_filter = ('author__username',) # agregar filtros

    # categories al ser manytomany hay que hacerlo de la siguiente manera..
    def post_categories(self, obj):
        return ', '.join([cat.name for cat in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorías'

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)