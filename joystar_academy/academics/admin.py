from django.contrib import admin

from .models import SubjectArea, TeachingApproach


@admin.register(SubjectArea)
class SubjectAreaAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)


@admin.register(TeachingApproach)
class TeachingApproachAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)