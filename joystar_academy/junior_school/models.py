from django.db import models


class JuniorSchoolHighlight(models.Model):
    """Highlights specific to the Junior School (Grade 7-8) pathway page."""

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, default="foundation")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class LearningPathway(models.Model):
    """Career/subject pathway options under CBC Junior School, e.g. STEM, Arts & Sports."""

    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name