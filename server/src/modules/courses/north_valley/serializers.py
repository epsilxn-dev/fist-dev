from datetime import datetime

from django.conf import settings
from rest_framework import serializers

from src.core.exception import ServerException


class NorthValleyRegistrationSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()

    def update(self, instance, validated_data):
        raise ServerException("Произошла непредвиденная ошибка")

    def create(self, validated_data):
        wks = settings.GSPREAD_CLIENT.open(settings.NORTH_VALLEY_SHEET_NAME).sheet1
        wks.append_row(
            [
                len(wks.col_values(1)) + 1,
                validated_data.get("name"),
                validated_data.get("email"),
                validated_data.get("phone"),
                datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                validated_data.get("user_agent"),
                validated_data.get("ip")
            ]
        )
        return validated_data
