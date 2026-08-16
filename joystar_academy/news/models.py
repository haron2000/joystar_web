from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class NewsCategory(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=90, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "News categories"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class NewsPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.ForeignKey(
        NewsCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts"
    )
    cover_image = models.ImageField(upload_to="news/covers/", blank=True, null=True)
    excerpt = models.CharField(max_length=300)
    body = models.TextField()
    author_name = models.CharField(max_length=120, default="Carol & Kelly Joystar Academy")
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField()

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("news:detail", args=[self.slug])

    def __str__(self):
        return self.title