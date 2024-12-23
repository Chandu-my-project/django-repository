from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from embed_video.admin import AdminVideoMixin

@admin.register(Discipline)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Program)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Career)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(Specialization)
class ViewAdmin(ImportExportModelAdmin):
    pass

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

