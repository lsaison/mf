from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app import views


urlpatterns = [
    path('', views.index, name='index'),
    path('produit/', views.produit, name='produit'),
    path('blog/', views.blog, name='blog'),
    path('blog_card/', views.blog_card, name='blog_card'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

