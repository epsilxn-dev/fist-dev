from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet

from src.modules.user.identification.auth import AuthenticationSystem
from .models import Direction, FistLessoner
from .serializers import DirectionSerializer, LessonerSerializer


class DirectionViewSet(ReadOnlyModelViewSet):
    queryset = Direction.objects.filter(is_deleted=False)
    authentication_classes = [AuthenticationSystem]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = DirectionSerializer
    swagger_tags = ["Fist school directions"]


class LessonerViewSet(ReadOnlyModelViewSet):
    queryset = FistLessoner.objects.all()
    authentication_classes = [AuthenticationSystem]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = LessonerSerializer
    swagger_tags = ["Fist school lessoners"]
