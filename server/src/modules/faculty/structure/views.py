from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import *


class DepartmentView(ReadOnlyModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    swagger_tags = ["Departments"]

    def retrieve(self, request: Request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            department = Department.objects.get(id=pk)
            specialties = department.specialty_set.all()
            lessoners = department.lessoner_set.all()
            data = {
                "department": DepartmentSerializer(department).data,
                "specialties": SpecialtySerializer(specialties, many=True).data,
                "lessoners": LessonerSerializer(lessoners, many=True).data
            }
            return Response(data, status=200)
        except Exception as e:
            return Response(status=404)


class SpecialtyView(ReadOnlyModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    swagger_tags = ["Specialties"]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            specialty = Specialty.objects.get(id=pk)
            disciplines = specialty.discipline_set.all()
            results = specialty.results_set.all()
            data = {
                "specialty": SpecialtySerializer(specialty).data,
                "disciplines": DisciplineSerializer(disciplines, many=True).data,
                "results": ResultSerializer(results, many=True).data
            }
            return Response(data, status=200)
        except Exception as e:
            return Response(status=404)


class DisciplineView(ReadOnlyModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer
    swagger_tags = ["Disciplines"]

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        try:
            discipline = Discipline.objects.get(id=pk)
            lessoners = discipline.lessoner_set.all()
            data = {
                "discipline": DisciplineSerializer(discipline).data,
                "lessoners": LessonerSerializer(lessoners, many=True).data
            }
            return Response(data, status=200)
        except Exception as e:
            return Response(status=404)


class LessonerView(ReadOnlyModelViewSet):
    queryset = Lessoner.objects.all()
    serializer_class = LessonerSerializer
    swagger_tags = ["Lessoners"]


class GraduateView(ReadOnlyModelViewSet):
    queryset = Graduate.objects.all()
    serializer_class = GraduateSerializer
    swagger_tags = ["Graduates"]
