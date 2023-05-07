from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .models import Vacancy, Company, Resume
from .serializers import VacancySerializer, CompanySerializer, ProceedResumeSerializer, GetResumeSerializer
from ...core.exception import ClientException


class CompanyView(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    swagger_tags = ["Companies"]


class VacancyView(ReadOnlyModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    swagger_tags = ["Vacancies"]


class ResumeView(ModelViewSet):
    queryset = Resume.objects.filter(is_moderated=True, is_deleted=False)
    serializer_class = GetResumeSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    swagger_tags = ["Resumes"]
    choice = ["Мужской", "Женский", "Не указан"]

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return ProceedResumeSerializer
        else:
            return self.serializer_class

    def retrieve(self, request: Request, *args, **kwargs):
        try:
            resume = Resume.objects.get(id=kwargs.get("pk"))
            if request.user.id == resume.id_id:
                serializer = super().get_serializer(resume)
                data = {**serializer.data}
                data["spec_name"] = resume.specialization.name
                return Response(data, status=200)
            else:
                resume = Resume.objects.get(id=kwargs.get("pk"), is_deleted=False, is_moderated=True)
                resume.views += 1
                serializer = super().get_serializer(resume)
                resume.save()
                data = {**serializer.data}
                data["spec_name"] = resume.specialization.name
                return Response(data, status=200)
        except Exception as e:
            raise ClientException(resp_status=404)

    def create(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer_class()
        candidates = Resume.objects.filter(id_id=request.user.id)
        if len(candidates) == 1:
            return Response(GetResumeSerializer(candidates[0]).data)
        data = serializer(data=request.data)
        if not data.is_valid():
            raise ClientException(data.errors)
        data.validated_data["user_id"] = request.user.id
        data.save()
        return Response(data.data)

    def partial_update(self, request: Request, *args, **kwargs):
        serializer = self.get_serializer_class()
        candidates = Resume.objects.filter(id_id=request.user.id)
        if len(candidates) != 1:
            raise ClientException()
        data = serializer(candidates[0], data=request.data)
        if not data.is_valid():
            raise ClientException(data.errors)
        data.save()
        return Response(data.data)

    def destroy(self, request: Request, *args, **kwargs):
        candidates = Resume.objects.filter(id_id=request.user.id, is_deleted=False)
        if len(candidates) != 1:
            raise ClientException()
        resume = candidates[0]
        resume.is_deleted = True
        resume.is_moderated = False
        resume.views = 0
        resume.save()
        return Response(status=204)
