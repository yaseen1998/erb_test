try:
    from django.db.models import JSONField
except ImportError:
    from django.contrib.postgres.fields import JSONField  # noqa