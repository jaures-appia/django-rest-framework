from rest_framework import viewsets, filters
from .models import *
from .serializers import *

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
    
    
class CategoriesViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    
class SouscategorieViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Souscategorie.objects.all()
    serializer_class = SouscategorieSerializer
    
class ArticleViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
class CommentaireViewSet(viewsets.ModelViewSet):
    filter_backends = (DynamicSearchFilter,)
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer