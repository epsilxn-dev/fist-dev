from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Question
from .serializers import QuestionSerializer


class QuestionView(ModelViewSet):
    queryset = Question.objects.filter(is_ready_to_publish=True)
    serializer_class = QuestionSerializer
    permission_classes = [AllowAny]
    swagger_tags = ["Questions"]
    http_method_names = ["get", "post", "head"]

    def create(self, request: Request, *args, **kwargs):
        try:
            request.data["is_ready_to_publish"] = False
            serializer = super().get_serializer(Question.objects.create(**request.data))
            return Response(serializer.data, status=201)
        except Exception as e:
            return Response(status=400)
