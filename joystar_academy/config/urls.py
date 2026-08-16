from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic import TemplateView

from .sitemaps import EventSitemap, NewsSitemap, StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "events": EventSitemap,
    "news": NewsSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path("", include("core.urls")),
    path("admissions/", include("admissions.urls")),
    path("academics/", include("academics.urls")),
    path("junior-school/", include("junior_school.urls")),
    path("clubs/", include("clubs.urls")),
    path("gallery/", include("gallery.urls")),
    path("events/", include("events.urls")),
    path("news/", include("news.urls")),
    path("contact/", include("contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")