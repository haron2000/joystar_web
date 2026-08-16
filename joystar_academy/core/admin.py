from django.contrib import admin

from .models import (
    CoreValue,
    HeroSlide,
    Programme,
    PromiseItem,
    SiteSettings,
    StatCounter,
    Testimonial,
    WhyChooseUsItem,
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)


@admin.register(PromiseItem)
class PromiseItemAdmin(admin.ModelAdmin):
    list_display = ("text", "order")
    list_editable = ("order",)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("caption", "order", "is_active")
    list_editable = ("order", "is_active")


@admin.register(WhyChooseUsItem)
class WhyChooseUsItemAdmin(admin.ModelAdmin):
    list_display = ("title", "order")
    list_editable = ("order",)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "stage", "age_range", "order")
    list_editable = ("order",)
    list_filter = ("stage",)


@admin.register(StatCounter)
class StatCounterAdmin(admin.ModelAdmin):
    list_display = ("label", "value", "suffix", "order")
    list_editable = ("order",)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("author_name", "role", "order", "is_active")
    list_editable = ("order", "is_active")