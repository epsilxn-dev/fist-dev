from rest_framework import serializers

from src.core.exception import ServerException
from src.modules.faculty.laboratories.serializers import AreaSerializer
from src.modules.tags.serializer import TagSerializer
from src.modules.user.user.sersizliers import UserSerializer
from .models import Idea, Commentary, Link, User, Tags, Area


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["link"]


class CreateIdeaSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    information = serializers.CharField()
    tags = serializers.ListField(allow_empty=False)
    team = serializers.ListField(allow_empty=False)
    area_tech = serializers.ListField(allow_empty=False)
    image = serializers.ImageField(use_url=True, required=False)

    def create(self, validated_data):
        idea = Idea.objects.create(
            name=validated_data.get("name"),
            description=validated_data.get("description"),
            information=validated_data.get("information"),
            author_id=validated_data.get("user_id"),
            image=validated_data.get("image", "not-found.png")
        )
        for tag in validated_data.get("tags"):
            idea.tags.add(Tags.objects.get_or_create(name=tag)[0])
        for username in validated_data.get("team"):
            idea.team.add(User.objects.get(username=username))
        for tech in validated_data.get("area_tech"):
            idea.area_tech.add(Area.objects.get_or_create(title=tech)[0])
        idea.save()
        validated_data["image"] = idea.image
        return validated_data

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.information = validated_data.get("information")
        instance.tags.set([Tags.objects.get_or_create(name=tag)[0] for tag in validated_data["tags"]])
        instance.area_tech.set([Area.objects.get_or_create(title=tech)[0] for tech in validated_data["area_tech"]])
        instance.team.set([User.objects.get(username=username) for username in validated_data["team"]])
        if validated_data.get("image") is not None:
            instance.image = validated_data.get("image")
        instance.is_moderated = False
        instance.save()
        validated_data["image"] = instance.image
        return validated_data


class IdeaSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    author = UserSerializer(many=False, read_only=True)
    likes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    dislikes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    area_tech = AreaSerializer(many=True, read_only=False)
    team = UserSerializer(many=True, read_only=False)
    image = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.image.url
        except:
            return None

    class Meta:
        model = Idea
        fields = "__all__"


class CommentarySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    idea = serializers.IntegerField()
    message = serializers.CharField()
    parent_id = serializers.IntegerField(allow_null=True)

    def create(self, validated_data):
        instance = Commentary.objects.create(
            message=validated_data.get("message"),
            user_id=validated_data.get("user_id"),
            idea_id=validated_data.get("idea"),
            parent_id=validated_data.get("parent_id")
        )
        validated_data["id"] = instance.id
        return validated_data

    def update(self, instance, validated_data):
        raise ServerException()


class GetCommentarySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Commentary
        fields = "__all__"

