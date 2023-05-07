from rest_framework import serializers

from src.modules.tags.serializer import TagSerializer
from .models import *


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class TechsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techs
        fields = "__all__"


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = ["title"]


class SpecialtySerializer(serializers.ModelSerializer):
    stack_techs = TechsSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    department = DepartmentSerializer(many=False, read_only=True)
    avatar = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.avatar.url
        except:
            return None

    class Meta:
        model = Specialty
        fields = "__all__"


class DisciplineSerializer(serializers.ModelSerializer):
    specialties = SpecialtySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Discipline
        fields = "__all__"


class LessonerSerializer(serializers.ModelSerializer):
    disciplines = DisciplineSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    department = DepartmentSerializer(many=False, read_only=True)
    avatar = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.avatar.url
        except:
            return None

    class Meta:
        model = Lessoner
        fields = "__all__"
        ref_name = "les1"


class GraduateSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    specialty = SpecialtySerializer(many=False, read_only=True)
    avatar = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.avatar.url
        except:
            return None

    class Meta:
        model = Graduate
        fields = "__all__"
