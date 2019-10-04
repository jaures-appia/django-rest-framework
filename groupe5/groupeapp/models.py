from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    """Model definition for Categories."""
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_categorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Categories."""

        verbose_name = 'Categories'
        verbose_name_plural = 'Categoriess'

    def __str__(self):
        """Unicode representation of Categories."""
        return self.nom


class Souscategorie(models.Model):
    """Model definition for Souscategorie."""
    categorie = models.ForeignKey(Categories, related_name='categorie_souscategorie', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_souscategorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Souscategorie."""

        verbose_name = 'Souscategorie'
        verbose_name_plural = 'Souscategories'

    def __str__(self):
        """Unicode representation of Souscategorie."""
        return self.nom


class Article(models.Model):
    """Model definition for Article."""
    souscategorie = models.ForeignKey(Souscategorie, related_name='souscategorie_article', on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='image_souscategorie')
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.nom



class Commentaire(models.Model):
    """Model definition for Commentaire."""
    user = models.ForeignKey(User,related_name='User_commentaire',on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='commentaire_article', on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        pass
