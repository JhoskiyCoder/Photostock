from django.apps import AppConfig
from django.db.models.signals import post_migrate

class PhotoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photoapp'

    def ready(self):
        import photoapp.permissions  # Здесь добавлена строка для импорта файла с разрешениями
        post_migrate.connect(self.create_permissions, sender=self)

    def create_permissions(self, **kwargs):
        import photoapp.permissions  