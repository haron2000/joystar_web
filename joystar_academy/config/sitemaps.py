from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from events.models import Event
from news.models import NewsPost


class StaticViewSitemap(Sitemap):
    priority = 0.7
    changefreq = "monthly"

    def items(self):
        return [
            "core:home",
            "core:about",
            "admissions:admissions",
            "academics:academics",
            "junior_school:junior_school",
            "clubs:clubs",
            "gallery:gallery",
            "events:list",
            "news:list",
            "contact:contact",
        ]

    def location(self, item):
        return reverse(item)


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.date


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return NewsPost.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.published_at