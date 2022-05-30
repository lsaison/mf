from django.shortcuts import render
from app.models import Article, Produit, Presentation


def index(request):
    presentation = Presentation.objects.first()
    produits = Produit.objects.all()
    return render(request, 'index.html', {'produits':produits, 'presentation':presentation})

    # pdt = []
    # ateliers = []
    # for p in Produit.objects.filter(affiche=True).order_by('ordre'):
    #     pdt.append(p)
    # boutique = Section.objects.get(titre="Boutique")
    # for a in Atelier.objects.all().order_by('ordre'):
    #     ateliers.append(a)
    # return render(request, 'index.html', {'produits': pdt, 'boutique':boutique, 'ateliers':ateliers})

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