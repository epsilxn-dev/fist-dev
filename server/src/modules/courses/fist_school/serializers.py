from rest_framework import serializers
from .models import Direction, FistLessoner
from src.modules.tags.serializer import TagSerializer
from src.modules.faculty.structure.serializers import DepartmentSerializer


class LessonerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(many=False, read_only=True)

    class Meta:
        model = FistLessoner
        fields = "__all__"


class DirectionSerializer(serializers.ModelSerializer):
    lessoners = LessonerSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Direction
        fields = "__all__"
