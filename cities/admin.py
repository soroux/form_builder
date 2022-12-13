from django.contrib import admin

# Register your models here.
from cities.models import Country, City, RuralDistrict, County, Province

admin.site.register(Country)
admin.site.register(Province)
admin.site.register(County)
admin.site.register(RuralDistrict)
admin.site.register(City)
