from django.apps import AppConfig


class FakeAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fake_app'
