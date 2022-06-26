import uuid
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _





class User(AbstractUser):
    """User model."""


    customer = models.CharField(max_length=100)
    id = models.CharField(
        primary_key=True,max_length=20, default=uuid.uuid4().hex[:10] , editable=False, unique=True)
    
    def __str__(self):
        return self.username



class Company(models.Model):
    """Company model."""

    name = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    
def dynamic_fieldname_model_factory(fields_prefix):
    class AbstractModel(models.Model):

        class Meta:
            abstract = True

    AbstractModel.add_to_class(
        fields_prefix + '_title',
        models.CharField(max_length=255, blank=True, default=''),
    )
    return AbstractModel


class ModelOne(dynamic_fieldname_model_factory('someprefix1')):
    id = models.AutoField(primary_key=True)


class ModelTwo(dynamic_fieldname_model_factory('someprefix2')):
    id = models.AutoField(primary_key=True)
    

attrs = {
    'name': models.CharField(max_length=32),
    '__module__': 'account.models'
}
Animal = type("account", (models.Model,), attrs)