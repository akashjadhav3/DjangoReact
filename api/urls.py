from django.urls import path, include
from .views import ArticleGenericViewSet #ArticleViewSet
#ArticleList, ArticleDetails,ArticleListMixin,ArticleDetailsMixin,article_list, article_details
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('articles', ArticleGenericViewSet, basename='articles')



urlpatterns = [
    path('', include(router.urls)),
    # path('article/', article_list),
    # path('article/<int:pk>/', article_details),
    # path('articlelist/', ArticleList.as_view()),
    # path('articlelist/<int:id>/', ArticleDetails.as_view()),
    # path('articlelistmixin/', ArticleListMixin.as_view()),
    # path('articlelistmixin/<int:id>/', ArticleDetailsMixin.as_view()),
]