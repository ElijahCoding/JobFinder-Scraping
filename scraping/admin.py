from django.contrib import admin
from .models import *

class VacancyAdmin(admin.ModelAdmin):
    class Meta:
        model = Vacancy
    list_display = ('title', 'url', 'city', 'specialty', 'timestamp')

admin.site.register(City)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Specialty)
admin.site.register(Site)
admin.site.register(Url)