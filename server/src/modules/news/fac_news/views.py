from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from .models import News, NewsCommentary
from .serializers import NewsCommentarySerializer, NewsSerializer


class NewsView(ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    swagger_tags = ["News"]
    search_fields = ["title", "text", "description"]
    ordering_fields = ["created_at", "id"]


class CommentaryView(ModelViewSet):
    queryset = NewsCommentary.objects.all()
    serializer_class = NewsCommentarySerializer
    swagger_tags = ["Commentaries (news)"]
    http_method_names = ["get", "post", "delete"]
    filterset_fields = ["news"]
    # pagination_class = None

    def create(self, request: Request, *args, **kwargs):
        comment = NewsCommentary.objects.create(
            text=request.data["text"],
            author_id=request.user.id,
            news_id=request.data["news"],
            parent_id=request.data.get("parent_id", None)
        )
        return Response(NewsCommentarySerializer(comment).data, status=201)

    def destroy(self, request: Request, *args, **kwargs):
        # Удаление верхнего комментария (родительского) приведёт к тому, что удалится родительский, но не удалятся
        # дочерние
        pk = kwargs["pk"]
        comment = NewsCommentary.objects.get(id=pk)
        if request.user.id == comment.author.id:
            return super().destroy(request, *args, **kwargs)
        return Response(status=403)

