from django.db import models
from django.db import connection, migrations, models
from django.db.migrations.executor import MigrationExecutor
from django.urls import clear_url_caches
from importlib import import_module,reload
from django.conf import settings
from django.contrib import admin

from django.core.validators import ValidationError

class App(models.Model):
    name = models.CharField(max_length=255)
    module = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Model(models.Model):
    # app = models.ForeignKey(App, related_name='models', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_django_model(self):
        "Returns a functional Django model based on current data"
        # Get all associated fields into a list ready for dict()
        for i in self.fields.all() : 
            print(i.name, i.type,'hhh')
            
        fields = [(f.name, f.get_django_field()) for f in self.fields.all()]

        # Use the create_model function defined above
        return create_model(self.name, dict(fields),  'fake_app','fake_app.models')

    # class Meta:
    #     unique_together = ( 'name',)

def is_valid_field(self, field_data = 'CharField'):
    if hasattr(models, field_data) and issubclass(getattr(models, field_data), models.Field):
        # It exists and is a proper field type
        return
    raise ValidationError("This is not a valid field type.")

class Field(models.Model):
    model = models.ForeignKey(Model, related_name='fields', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, validators=[is_valid_field])

    def get_django_field(self):
        "Returns the correct field type, instantiated with applicable settings"
        # Get all associated settings into a list ready for dict()
        settings = [(s.name, s.value) for s in self.settings.all()]

        # Instantiate the field with the settings as **kwargs
        return getattr(models, self.type)(**dict(settings))

    class Meta:
        unique_together = (('model', 'name'),)

class Setting(models.Model):
    field = models.ForeignKey(Field, related_name='settings', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = (('field', 'name'),)
        
        
def create_model(name, fields=None, app_label=None, module='', options=None, admin_opts=None):
    """
    Create specified model
    """
    class Meta:
        db_table = name
    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)
    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.items():
            setattr(Meta, key, value)
    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}
    # Add in any fields that were provided
    if fields:
        attrs.update(fields)
    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)
    # admin.site.register(model)
    # reload(import_module(settings.ROOT_URLCONF))
    # clear_url_caches()
    
    
    return model


class Test(models.Model):
    name = models.IntegerField()
   
