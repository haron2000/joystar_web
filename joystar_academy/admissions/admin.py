from django.contrib import admin

from .models import AdmissionInquiry, AdmissionStep, RequiredDocument


@admin.register(AdmissionStep)
class AdmissionStepAdmin(admin.ModelAdmin):
    list_display = ("step_number", "title")


@admin.register(RequiredDocument)
class RequiredDocumentAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)


@admin.register(AdmissionInquiry)
class AdmissionInquiryAdmin(admin.ModelAdmin):
    list_display = ("parent_name", "request_type", "phone", "email", "submitted_at", "is_handled")
    list_filter = ("request_type", "is_handled")
    search_fields = ("parent_name", "email", "phone", "child_name")