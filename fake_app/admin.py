from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(App)
admin.site.register(Model)
admin.site.register(Setting)
admin.site.register(Field)
admin.site.register(Test)

# for model in ["Popo"]:
#     reg_model = Model.objects.get(name=model).get_django_model()
#     admin.site.register(reg_model)