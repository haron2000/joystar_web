from django.shortcuts import render

from .models import GalleryCategory, GalleryImage


def gallery(request):
    category_slug = request.GET.get("category")
    images = GalleryImage.objects.select_related("category")
    if category_slug:
        images = images.filter(category__slug=category_slug)

    context = {
        "meta_description": (
            "Browse photos from Carol & Kelly Joystar Academy — sports, academics, robotics, "
            "trips, arts, music and school events."
        ),
        "categories": GalleryCategory.objects.all(),
        "images": images,
        "active_category": category_slug or "all",
    }
    return render(request, "gallery.html", context)