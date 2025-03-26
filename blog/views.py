from django.shortcuts import render, get_list_or_404
from .models import Post, Category

# Create your views here.
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', { 'posts': posts })

def cateogory(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', { 'posts': posts })