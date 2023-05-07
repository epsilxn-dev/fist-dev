from rest_framework import serializers

from src.modules.faculty.structure.serializers import SpecialtySerializer
from src.modules.tags.serializer import TagSerializer
from src.modules.user.user.sersizliers import UserSerializer
from src.modules.tags.models import Tags
from .models import Vacancy, Company, Resume, Skill
from ...core.exception import ClientException, ServerException


class CompanySerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.avatar.url
        except:
            return None

    class Meta:
        model = Company
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"


class GetResumeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    tags = SkillSerializer(many=True, read_only=True)
    id = UserSerializer()
    image = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.image.url
        except:
            return None

    class Meta:
        model = Resume
        # fields = "__all__"
        exclude = ["is_deleted", "is_moderated"]


class ProceedResumeSerializer(serializers.Serializer):
    image = serializers.ImageField(use_url=True, required=False)
    title = serializers.CharField(max_length=30, min_length=5)
    description = serializers.CharField()
    gender = serializers.CharField()
    phone = serializers.CharField()
    email = serializers.EmailField()
    salary = serializers.CharField(min_length=4)
    specialization_id = serializers.IntegerField()
    skills = serializers.ListSerializer(child=serializers.CharField())
    tags = serializers.ListSerializer(child=serializers.CharField())
    work_exp = serializers.CharField()

    def update(self, instance: Resume, validated_data):
        instance.title = validated_data.get("title")
        instance.description = validated_data.get("description")
        instance.salary = validated_data.get("salary")
        instance.phone = validated_data.get("phone")
        instance.email = validated_data.get("email")
        instance.work_exp = validated_data.get("work_exp")
        instance.gender = validated_data.get("gender")
        instance.specialization_id = validated_data.get("specialization_id")
        instance.is_moderated = False
        instance.is_deleted = False
        if validated_data.get("image") is not None:
            instance.image = validated_data.get("image")
        _skills = [(Skill.objects.get_or_create(name=item))[0].id for item in validated_data.get("skills")]
        tags = [(Tags.objects.get_or_create(name=item))[0].id for item in validated_data.get("tags")]
        instance.skills.set(_skills)
        instance.tags.set(tags)
        validated_data["image"] = instance.image
        instance.save()
        return validated_data

    def create(self, validated_data):
        resume = None
        try:
            resume = Resume.objects.create(
                id_id=validated_data.get("user_id"),
                title=validated_data.get("title"),
                description=validated_data.get("description"),
                salary=validated_data.get("salary"),
                phone=validated_data.get("phone"),
                email=validated_data.get("email"),
                image=validated_data.get("image", "not-found.png"),
                work_exp=validated_data.get("work_exp"),
                gender=validated_data.get("gender"),
                specialization_id=validated_data.get("specialization_id")
            )
        except Exception as e:
            raise ClientException("У вас уже есть созданное резюме!", resp_status=400)
        _skills = [(Skill.objects.get_or_create(name=item))[0].id for item in validated_data.get("skills")]
        tags = [(Tags.objects.get_or_create(name=item))[0].id for item in validated_data.get("tags")]
        resume.skills.set(_skills)
        resume.tags.set(tags)
        validated_data["image"] = resume.image
        resume.save()
        return validated_data


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer(many=False, read_only=False)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = "__all__"
