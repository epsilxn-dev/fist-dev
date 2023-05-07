from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from src.core.exception import ClientException

from .models import Idea, Commentary
from .serializers import IdeaSerializer, CommentarySerializer, CreateIdeaSerializer, GetCommentarySerializer
from ...user.user.sersizliers import UserSerializer


class IdeaView(ModelViewSet):
    queryset = Idea.objects.filter(is_moderated=True)
    serializer_class = IdeaSerializer
    filterset_fields = ["author"]
    swagger_tags = ["Ideas"]
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return IdeaSerializer
        elif self.action == "create" or self.action == "partial_update":
            return CreateIdeaSerializer

    def list(self, request, *args, **kwargs):
        author_param = request.query_params.get("author")
        serializer = self.get_serializer_class()
        if author_param:
            if request.user.id == int(author_param):
                ideas = IdeaSerializer(Idea.objects.filter(author_id=request.user.id), many=True).data
                return Response(ideas, status=200)
        user_ideas = Idea.objects.filter(author_id=request.user.id)
        all_ideas = Idea.objects.filter(is_moderated=True)
        result_set = user_ideas | all_ideas
        data = serializer(result_set, many=True).data
        return Response(data)

    def retrieve(self, request: Request, *args, **kwargs):
        idea_id = int(kwargs.get("pk"))
        candidates = Idea.objects.filter(id=idea_id)
        if len(candidates) != 1:
            raise ClientException("Не найдено", 404)
        idea = candidates[0]
        serializer = self.get_serializer_class()
        data = serializer(idea, many=False).data
        if request.user.id != idea.author_id and not idea.is_moderated:
            raise ClientException("Не найдено", 404)
        return Response(data, status=200)

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer_class()
        validated_data = serializer(data=request.data)
        if not validated_data.is_valid():
            raise ClientException(validated_data.errors)
        validated_data.save(user_id=request.user.id)
        return Response(validated_data.data, status=201)

    def partial_update(self, request: Request, *args, **kwargs):
        idea = Idea.objects.get(id=kwargs.get("pk"))
        if request.user.id == idea.author_id:
            serializer = self.get_serializer_class()
            data = serializer(idea, data=request.data)
            if not data.is_valid():
                raise ClientException(data.errors)
            data.save()
            return Response(data.data)
        raise ClientException(resp_status=403)

    def destroy(self, request, *args, **kwargs):
        idea = Idea.objects.get(id=kwargs.get("pk"))
        if request.user.id == idea.author_id:
            idea.delete()
            return Response(status=204)
        else:
            raise ClientException(resp_status=403)


class LikeView(CreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]
    swagger_tags = ["Ideas"]

    def create(self, request: Request, *args, **kwargs):
        request_idea_id = request.data.get("id")
        try:
            idea = Idea.objects.get(id=request_idea_id)
            if idea in request.user.likes.all():  # если идея уже в лайках юзера
                request.user.likes.remove(idea)  # то удаляем из лайков (как в вк, когда пользователь повторно нажимает на лайк)
                flag = False  # флаг нужен для клиентской части
            else:
                if idea in request.user.dislikes.all():
                    # если стоит дизлайк, то надо его убрать
                    request.user.dislikes.remove(idea)
                idea.likes.add(request.user)  # и влепить лайк
                flag = True
                idea.save()
        except Exception as e:
            return Response(str(e), status=400)
        return Response(flag, status=200)


class DislikeView(CreateAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    permission_classes = [IsAuthenticated]
    swagger_tags = ["Ideas"]

    def create(self, request: Request, *args, **kwargs):
        request_idea_id = request.data.get("id")
        try:
            idea = Idea.objects.get(id=request_idea_id)
            if idea in request.user.dislikes.all():  # аналогично с LikeView, только теперь с дизлайками
                request.user.dislikes.remove(idea)
                flag = False
            else:
                if idea in request.user.likes.all():
                    request.user.likes.remove(idea)
                idea.dislikes.add(request.user)
                flag = True
                idea.save()
        except Exception as e:
            return Response(str(e), status=400)
        return Response(flag, status=200)


class CommentaryView(ModelViewSet):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    filterset_fields = ["idea"]
    http_method_names = ["get", "post", "delete"]
    swagger_tags = ["Idea`s Commentary"]

    def get_serializer_class(self):
        if self.action in ["create", "destroy"]:
            return CommentarySerializer
        else:
            return GetCommentarySerializer

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer_class()
        data = serializer(data=request.data)
        if not data.is_valid():
            raise ClientException(data.errors)
        data.save(user_id=request.user.id)
        data.validated_data["user"] = UserSerializer(request.user).data
        data.validated_data["id"] = data.instance["id"]
        return Response(data.validated_data, status=200)

    def destroy(self, request, *args, **kwargs):
        comment = Commentary.objects.get(id=int(kwargs.get("pk")))
        if request.user.id == comment.user_id:
            return super().destroy(request, *args, **kwargs)
        raise ClientException(resp_status=403)
