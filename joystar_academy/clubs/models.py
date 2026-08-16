from django.db import models
from django.utils.text import slugify


class Club(models.Model):
    """A club or co-curricular activity, e.g. Coding & Robotics, Chess Club."""

    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    summary = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="clubs/", blank=True, null=True)
    icon = models.CharField(max_length=50, default="foundation")
    meeting_day = models.CharField(max_length=100, blank=True, help_text="e.g. Every Tuesday, 2:00 - 3:00 PM")
    is_sport = models.BooleanField(
        default=False, help_text="Check if this is a sports/talent-development activity rather than a club."
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name