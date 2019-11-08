from django.contrib import admin

from edu import models


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    pass
