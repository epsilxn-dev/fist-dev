from rest_framework import serializers

from src.modules.tags.serializer import TagSerializer
from src.modules.user.user.sersizliers import UserSerializer
from .models import News, NewsCommentary


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    image = serializers.SerializerMethodField("image_field")

    def image_field(self, obj):
        try:
            return obj.image.url
        except:
            return None

    class Meta:
        model = News
        fields = "__all__"


class NewsCommentarySerializer(serializers.ModelSerializer):
    author = UserSerializer(many=False, read_only=True)
    news = serializers.PrimaryKeyRelatedField(many=False, read_only=False, queryset=NewsCommentary.objects.all())

    class Meta:
        model = NewsCommentary
        fields = "__all__"

