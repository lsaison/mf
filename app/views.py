from django.shortcuts import render
from app.models import Article, Produit


def index(request):
    produits = Produit.objects.all()
    return render(request, 'index.html', {'produits':produits})

def produit(request):
    produits = Produit.objects.all()
    return render(request, 'guidage.html', {'produits':produits})

def blog_card(request):
    return render(request, 'blog_card.html')

def test(request):
    return render(request, 'test.html')

def blog(request):
    articles = Article.objects.all()
    return render(request, 'blog.html', {"articles":articles})