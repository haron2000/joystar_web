from django.db import models


class AdmissionStep(models.Model):
    """A step in the admissions process, shown as a numbered timeline."""

    step_number = models.PositiveIntegerField()
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["step_number"]

    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class RequiredDocument(models.Model):
    name = models.CharField(max_length=150)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name


class AdmissionInquiry(models.Model):
    """Captures 'Apply Now' / 'Book a Visit' form submissions."""

    class RequestType(models.TextChoices):
        APPLY = "apply", "Apply Now"
        VISIT = "visit", "Book a Visit"

    request_type = models.CharField(max_length=10, choices=RequestType.choices, default=RequestType.APPLY)
    parent_name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    child_name = models.CharField(max_length=120, blank=True)
    desired_programme = models.CharField(max_length=100, blank=True)
    preferred_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_handled = models.BooleanField(default=False)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return f"{self.get_request_type_display()} — {self.parent_name}"