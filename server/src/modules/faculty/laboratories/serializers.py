from rest_framework import serializers

from src.modules.faculty.structure.serializers import SpecialtySerializer
from src.modules.tags.serializer import TagSerializer
from src.modules.user.user.sersizliers import UserSerializer
from .models import *


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = "__all__"


class LaboratorySerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.image.url
        except:
            return None

    class Meta:
        model = Laboratory
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    teamlead = UserSerializer(many=False, read_only=True)
    lab = LaboratorySerializer(many=False, read_only=True)
    areas = AreaSerializer(many=True, read_only=True)
    specialty = SpecialtySerializer(many=False, read_only=True)
    contributors = UserSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField("image_field")
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    dislikes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def image_field(self, obj):
        try:
            return obj.image.url
        except:
            return None

    class Meta:
        model = Project
        fields = "__all__"
