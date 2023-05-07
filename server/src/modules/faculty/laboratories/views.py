from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import *


class ProjectView(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    swagger_tags = ["Projects"]


class LikeView(CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    swagger_tags = ["Projects"]

    def create(self, request: Request, *args, **kwargs):
        request_idea_id = request.data.get("id")
        try:
            project = Project.objects.get(id=request_idea_id)
            if project in request.user.project_likes.all():  # если лайк уже стоит
                request.user.project_likes.remove(project)  # то удаляем его (как в вк)
                flag = False  # для клиентской стороны
            else:
                if project in request.user.project_dislikes.all():  # иначе, если стоит дизлайк
                    request.user.project_dislikes.remove(project)  # то удаляем его
                project.likes.add(request.user)  # и ставим лайк
                flag = True
                project.save()
        except Exception as e:
            print(f"{request.method} {request.path}:", str(self), str(e))
            return Response(str(e), status=400)
        return Response(flag, status=200)


class DislikeView(CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated]
    swagger_tags = ["Projects"]

    def create(self, request: Request, *args, **kwargs):
        request_idea_id = request.data.get("id")
        try:
            project = Project.objects.get(id=request_idea_id)
            if project in request.user.project_dislikes.all():  # аналогично лайкам
                request.user.project_dislikes.remove(project)
                flag = False
            else:
                if project in request.user.project_likes.all():
                    request.user.project_likes.remove(project)
                project.dislikes.add(request.user)
                flag = True
                project.save()
        except Exception as e:
            print(f"{request.method} {request.path}:", str(self), str(e))
            return Response(str(e), status=400)
        return Response(flag, status=200)


class LaboratoryView(ReadOnlyModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
    swagger_tags = ["Laboratories"]

    def retrieve(self, request, *args, **kwargs):
        lab_id = kwargs.get("pk")
        lab = Laboratory.objects.get(id=lab_id)
        projects = lab.project_set.filter(lab_id=lab_id)
        response_data = {
            "lab": LaboratorySerializer(lab).data,
            "projects": ProjectSerializer(projects, many=True).data
        }
        return Response(response_data, status=200)
