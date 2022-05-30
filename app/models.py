from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Presentation(models.Model):
    img = models.ImageField(upload_to='img/', blank=True, null=True, help_text="300px x 300px")
    imgAlt = models.CharField(max_length=255, blank=True)
    titre = models.CharField(max_length=100)
    texte = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.titre}"

class Article(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    affiche = models.BooleanField()
    ordre = models.PositiveSmallIntegerField(unique=True,validators=[MinValueValidator(1), MaxValueValidator(100)])
    # content = RichTextField(blank=True, null=True)
    content_upload = RichTextUploadingField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.ordre} - {self.titre}"



class Produit(models.Model):
    ref = models.CharField(max_length=100, unique=True)
    lib1 = models.CharField(max_length=255)
    affiche = models.BooleanField()
    ordre = models.PositiveSmallIntegerField(unique=True,validators=[MinValueValidator(1), MaxValueValidator(100)])
    lib2 = models.CharField(max_length=255, blank=True)
    desc = models.TextField(blank=True, null=True)
    durée = models.CharField(max_length=100, blank=True)
    puht = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
    promo = models.BooleanField()
    nouveau = models.BooleanField()
    presentation = models.BooleanField()
    img = models.ImageField(upload_to='img/', blank=True, null=True, help_text="300px x 300px")
    imgAlt = models.CharField(max_length=255, blank=True)

    
    def __str__(self):
        return f"{self.ordre} - {self.lib1}"