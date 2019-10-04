from rest_framework.routers import DefaultRouter
from .apiviews import *

router = DefaultRouter()
router.register('commentaire', CommentaireViewSet, base_name='commentaire')
router.register('article', ArticleViewSet, base_name='article')
router.register('sous', SouscategorieViewSet, base_name='sous')
router.register('categorie', CategoriesViewSet, base_name='categorie')

urlpatterns = [
    # ...
]

urlpatterns += router.urls
