from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(student_points)

@admin.register(personality)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(cluster)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(personality_cluster)
class ViewAdmin(ImportExportModelAdmin):
    pass

@admin.register(cluster_major)
class ViewAdmin(ImportExportModelAdmin):
    pass

