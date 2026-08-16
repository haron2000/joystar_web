from django.contrib import admin

from .models import JuniorSchoolHighlight, LearningPathway


@admin.register(JuniorSchoolHighlight)
class JuniorSchoolHighlightAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(LearningPathway)
class LearningPathwayAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)