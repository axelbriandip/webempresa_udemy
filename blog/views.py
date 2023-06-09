from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def blog (request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', { 'posts': posts })

# forma rudimentaria de filtrar por categoría
# def category (request, category_id):
#     # category = Category.objects.get(id=category_id)
#     category = get_object_or_404(Category, id=category_id)
#     posts_filtered = Post.objects.filter(categories = category)
#     return render(request, 'blog/category.html', { 'category': category, 'posts_filtered': posts_filtered })

# forma más práctica de filtrar por categoría
def category (request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'blog/category.html', { 'category': category })