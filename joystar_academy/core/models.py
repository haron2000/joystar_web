from django.core.exceptions import ValidationError
from django.db import models


class SiteSettings(models.Model):
    """Singleton holding site-wide info: contact details, socials, vision/mission."""

    school_name = models.CharField(max_length=200, default="Carol and Kelly Joystar Academy")
    motto = models.CharField(max_length=200, default="Creating a Firm Foundation")
    phone = models.CharField(max_length=50, default="0700347587")
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, default="Umoja 1 Q46, Nairobi")
    map_embed_url = models.URLField(
        blank=True,
        help_text="Paste a Google Maps 'Embed a map' src URL here.",
    )
    vision = models.TextField(
        default=(
            "To be the school of choice for nurturing confident, responsible and "
            "globally competitive learners through quality education."
        )
    )
    mission = models.TextField(
        default=(
            "To nurture every learner's talents to excellence through quality education, "
            "innovation, love and strong Christian values in a safe and supportive environment."
        )
    )
    philosophy = models.TextField(
        default=(
            "Every child is unique and capable of success when given the right environment, "
            "guidance and opportunities to learn, explore and grow."
        )
    )
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    tiktok_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # prevent deleting the singleton

    def clean(self):
        if SiteSettings.objects.exclude(pk=self.pk).exists():
            raise ValidationError("Only one SiteSettings instance is allowed.")

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return self.school_name


class CoreValue(models.Model):
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class PromiseItem(models.Model):
    """A single line of the School Promise, e.g. 'We teach with care.'"""

    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.text


class HeroSlide(models.Model):
    """Slides for the homepage hero slideshow."""

    image = models.ImageField(upload_to="hero/")
    caption = models.CharField(max_length=150, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.caption or f"Slide {self.pk}"


class WhyChooseUsItem(models.Model):
    """e.g. Competency-Based Curriculum, Qualified Teachers, Coding & Robotics..."""

    title = models.CharField(max_length=120)
    description = models.CharField(max_length=255, blank=True)
    icon = models.CharField(
        max_length=50,
        default="foundation",
        help_text="Name of an icon defined in static/img/icons.svg",
    )
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Why Choose Us item"
        verbose_name_plural = "Why Choose Us items"

    def __str__(self):
        return self.title


class Programme(models.Model):
    """Academic programme / grade level, e.g. Playgroup, PP1, Grade 4, Junior School."""

    class Stage(models.TextChoices):
        EARLY_YEARS = "early_years", "Early Years"
        LOWER_PRIMARY = "lower_primary", "Lower Primary"
        UPPER_PRIMARY = "upper_primary", "Upper Primary"
        JUNIOR_SCHOOL = "junior_school", "Junior School"

    name = models.CharField(max_length=100)
    stage = models.CharField(max_length=20, choices=Stage.choices)
    age_range = models.CharField(max_length=50, blank=True)
    summary = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class StatCounter(models.Model):
    """Animated counters, e.g. '10+ Years', '500+ Learners'."""

    label = models.CharField(max_length=80)
    value = models.PositiveIntegerField()
    suffix = models.CharField(max_length=10, blank=True, default="+")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.value}{self.suffix} {self.label}"


class Testimonial(models.Model):
    author_name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True, help_text="e.g. Parent, Grade 5 Learner")
    quote = models.TextField()
    photo = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.author_name} ({self.role})"