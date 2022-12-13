from django.contrib import admin

# Register your models here.
from createForm.models import DataType, Attribute, DataAttribute

admin.site.register(DataType)
admin.site.register(Attribute)
admin.site.register(DataAttribute)
