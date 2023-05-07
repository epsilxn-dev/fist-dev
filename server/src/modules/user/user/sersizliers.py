from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        exclude = ["permissions"]


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    avatar = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.avatar.url
        except:
            return None

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "avatar", "discord", "skype", "groups",
                  "phone", "patronymic"]
