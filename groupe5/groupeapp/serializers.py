from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from .models import * 

class CommentaireSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'


class ArticleSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    commentaire_article = CommentaireSerializer(many=True, required=False)
    class Meta:
        model = Article
        fields = '__all__'


class SouscategorieSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    souscategorie_article = ArticleSerializer(many=True, required=False)
    class Meta:
        model = Souscategorie
        fields = '__all__'


class CategoriesSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    categorie_souscategorie = SouscategorieSerializer(many=True, required=False)
    class Meta:
        model = Categories
        fields = '__all__'
