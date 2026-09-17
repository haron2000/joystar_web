from django.db import models


class SubjectArea(models.Model):
    """A CBC learning area, e.g. Literacy, Mathematics, Creative Arts."""

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    icon = models.CharField(max_length=50, default="book")
    order = models.PositiveIntegerField(default=0)
    

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class TeachingApproach(models.Model):
    """e.g. Experiential Learning, Individual Attention, Small Class Sizes."""

    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title