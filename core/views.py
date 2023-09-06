from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = '''
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about-me/">About me</a></li>
        <li><a href="/portfolio/">Portfolio</a></li>
        <li><a href="/contact/">Contact</a></li>
    </ul>
'''

def home(request):
    return HttpResponse(html_base + "<h3>Este es el home</h3>")

def about_me(request):
    return HttpResponse(html_base + "<h3>Este es el about_me</h3>")

def portfolio(request):
    return HttpResponse(html_base + "<h3>Este es el portfolio</h3>")

def contact(request):
    return HttpResponse(html_base + "<h3>Este es el contact</h3>")