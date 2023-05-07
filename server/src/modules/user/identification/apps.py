import sys

from django.apps import AppConfig


class IdentificationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.modules.user.identification'

    def ready(self):
        from django.contrib.auth.models import Group, Permission, ContentType
        from django.conf import settings

        if "runserver" not in sys.argv:
            return True

        try:
            for role in settings.ROLES:
                Group.objects.get_or_create(name=role)
        except Exception as e:
            print(str(e))
            raise Exception("Необходимо применить миграции, чтобы запустить проект")