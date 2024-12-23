from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Subject)
admin.site.register(Quiz)
admin.site.register(Recommendation)
@admin.register(Degree)
class ViewAdmin(ImportExportModelAdmin):
    pass
