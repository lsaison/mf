from django.contrib import admin
from app.models import Article, Produit

# admin/makwa


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    fields = ('ref', 'affiche', 'presentation', 'ordre', 'lib1', 'lib2', 'desc',
              'puht', 'durée', 'promo', 'nouveau', 'img', 'imgAlt')
    list_display = ('ref', 'affiche','presentation', 'ordre', 'lib1', 'promo', 'nouveau', 'puht', 'durée')
    list_editable = ('affiche', 'ordre', 'presentation', 'lib1', 'promo', 'nouveau', 'puht', 'durée')
