from rest_framework import status, generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ArticleModel, CommentModel
from .serializers import ArticleSerializer, ArticleDetailSerializer, CommentCreateSerializer


class ArticleView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = ArticleSerializer
    queryset = ArticleModel.objects.all()

    def get(self, request, id=None):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleDetailSerializer
    queryset = ArticleModel.objects.all()


class CommentCreateView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = CommentCreateSerializer
    queryset = CommentModel.objects.all()

    def post(self, request):
        return self.create(request)
