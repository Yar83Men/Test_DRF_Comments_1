from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#from .views import ArticleListView, ArticleDetailView, ArticleCreateView, CommentCreateView,
from .views import ArticleView, ArticleDetailView, CommentCreateView

schema_view = get_schema_view(
   openapi.Info(
      title="Test API",
      default_version='v1',
      description="Test description",
      terms_of_service="",
      contact=openapi.Contact(email="yarik83.evpat@gmail.com"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('api/v1/articles/', ArticleListView.as_view()),
    # path('api/v1/article/<int:pk>/', ArticleDetailView.as_view()),
    # path('api/v1/article/create/', ArticleCreateView.as_view()),
    # path('api/v1/comment/create/', CommentCreateView.as_view()),
    path('api/v1/article/', ArticleView.as_view()),
    path('api/v1/article/<int:pk>', ArticleDetailView.as_view()),
    path('api/v1/comment/create/', CommentCreateView.as_view())
]