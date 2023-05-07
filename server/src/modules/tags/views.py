from urllib.parse import unquote

from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from src.modules.faculty.structure.serializers import SpecialtySerializer, DisciplineSerializer, LessonerSerializer
from src.modules.questions.serializers import QuestionSerializer
from src.modules.projects.ideas.serializers import IdeaSerializer
from src.modules.faculty.laboratories.serializers import LaboratorySerializer, ProjectSerializer
from src.modules.news.fac_news.serializers import NewsSerializer
from .filters import TagFilter
from .models import Tags
from .serializer import TagSerializer


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer
    filterset_class = TagFilter
    swagger_tags = ["Tags"]


class TagSearcher(APIView):
    swagger_tags = ["Tags"]
    permission_classes = [AllowAny]

    def get(self, request: Request, *args, **kwargs):
        try:
            tag = Tags.objects.filter(name=unquote(request.query_params["tag"]))[0]
            spec = SpecialtySerializer(tag.specialty_set.all(), many=True).data
            disciplines = DisciplineSerializer(tag.discipline_set.all(), many=True).data
            lessoners = LessonerSerializer(tag.lessoner_set.all(), many=True).data
            questions = QuestionSerializer(tag.question_set.all(), many=True).data
            ideas = IdeaSerializer(tag.idea_set.all(), many=True).data
            labs = LaboratorySerializer(tag.laboratory_set.all(), many=True).data
            projects = ProjectSerializer(tag.project_set.all(), many=True).data
            news = NewsSerializer(tag.news_set.all(), many=True).data
            data = {
                "specialties": spec,
                "disciplines": disciplines,
                "lessoners": lessoners,
                "questions": questions,
                "ideas": ideas,
                "labs": labs,
                "projects": projects,
                "news": news
            }
            response = Response(data=data, status=200)
        except Exception as e:
            response = Response(status=400)
        return response
