from django.contrib import admin

from .models import Club


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    list_display = ("name", "is_sport", "meeting_day", "order")
    list_editable = ("order",)
    list_filter = ("is_sport",)
    prepopulated_fields = {"slug": ("name",)}