from rest_framework import serializers
from src.modules.tags.serializer import TagSerializer
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=False)

    class Meta:
        model = Question
        fields = "__all__"
