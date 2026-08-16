from django.contrib import admin

from .models import Event, EventAttachment, EventCategory, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1


class EventAttachmentInline(admin.TabularInline):
    model = EventAttachment
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "venue")
    list_filter = ("category", "date")
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [EventImageInline, EventAttachmentInline]


@admin.register(EventCategory)
class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    prepopulated_fields = {"slug": ("name",)}