from django.contrib import admin, messages
from django.shortcuts import redirect, render
from django.urls import path

from .forms import BulkGalleryUploadForm
from .models import GalleryCategory, GalleryImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("caption", "category", "uploaded_at")
    list_filter = ("category",)
    change_list_template = "admin/gallery/galleryimage/change_list.html"

    def get_urls(self):
        custom_urls = [
            path(
                "bulk-upload/",
                self.admin_site.admin_view(self.bulk_upload),
                name="gallery_galleryimage_bulk_upload",
            ),
        ]
        return custom_urls + super().get_urls()

    def bulk_upload(self, request):
        if request.method == "POST":
            form = BulkGalleryUploadForm(request.POST, request.FILES)
            if form.is_valid():
                category = form.cleaned_data["category"]
                images = form.cleaned_data["images"]
                for f in images:
                    GalleryImage.objects.create(category=category, image=f)
                self.message_user(
                    request, f"Uploaded {len(images)} photo(s) to {category.name}.", messages.SUCCESS
                )
                return redirect("..")
        else:
            form = BulkGalleryUploadForm()

        context = dict(
            self.admin_site.each_context(request),
            form=form,
            title="Bulk upload gallery photos",
        )
        return render(request, "admin/gallery/bulk_upload.html", context)