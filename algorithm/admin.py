from django.contrib import admin
from .models import Algorithm



class AlgorithmAdmin(admin.ModelAdmin):
    list_filter = ['result']




admin.site.register(Algorithm, AlgorithmAdmin)
