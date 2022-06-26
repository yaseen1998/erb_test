from django.db import models
from django.db import connection, migrations, models
from django.db.migrations.executor import MigrationExecutor
from django.urls import clear_url_caches
from importlib import import_module,reload
from django.conf import settings
from django.contrib import admin


fields = dict(
    title = models.TextField(db_column='Title', blank=True, null=True),
    url = models.CharField(db_column='Url', unique=True, max_length=250, blank=True, null=True),
    description = models.TextField(db_column='Description', blank=True, null=True),
    created_at = models.DateTimeField(db_column='Created_at'),
)


from django.apps import apps
def create_models(name, fields=None, app_label=None, module='', options=None, admin_opts=None):
    """
    Create specified model
    """
    create_table(f'{name}', fields, app_label)
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
    admin.site.register(model)
    reload(import_module(settings.ROOT_URLCONF))
    clear_url_caches()
    try:
        apps.get_model('fake_app', name)
    except KeyError:
        pass
    
    return model


def create_table(table_name, model_fields, app_label):
    class Migration(migrations.Migration):
        initial = True
        dependencies = []
        operations = [
            migrations.CreateModel(
                name=table_name,
                fields=[
                    ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ] + [(k, field) for k,field in model_fields.items()],
                options={
                    'db_table': table_name,
                },
            ),
        ]
    executor = MigrationExecutor(connection)
    migration = Migration(table_name, app_label)
    with connection.schema_editor(atomic=True) as schema_editor:
        migration.apply(executor._create_project_state(), schema_editor)
        
        
        
def model_to_dict(model):
    """
    Convert a model instance into a dict
    """
    opts = model._meta
    data = {}
    for f in opts.concrete_fields:
        data[f.name] = getattr(model, f.attname)
    for f in opts.many_to_many:
        data[f.name] = list(getattr(model, f.name).values_list('pk', flat=True))
    return data