from drf_yasg.inspectors import SwaggerAutoSchema


class MainSwaggerSchema(SwaggerAutoSchema):
    """
    Класс нужен для генерации схемы в сваггере. По сути, его можно вообще не трогать
    """

    def get_tags(self, operation_keys=None):
        tags = self.overrides.get('tags', None) or getattr(self.view, 'swagger_tags', [])
        if not tags:
            tags = [operation_keys[0]]

        return tags