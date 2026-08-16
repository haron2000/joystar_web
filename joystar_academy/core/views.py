from django.shortcuts import render
from django.utils import timezone

from academics.models import SubjectArea
from clubs.models import Club
from events.models import Event
from gallery.models import GalleryImage
from news.models import NewsPost

from .models import (
    CoreValue,
    HeroSlide,
    Programme,
    PromiseItem,
    StatCounter,
    Testimonial,
    WhyChooseUsItem,
)


def home(request):
    context = {
        "meta_description": (
            "Carol & Kelly Joystar Academy in Umoja, Nairobi — a CBC school nurturing "
            "confident, responsible learners from Playgroup to Junior School. Creating a Firm Foundation."
        ),
        "hero_slides": HeroSlide.objects.filter(is_active=True),
        "why_choose_us": WhyChooseUsItem.objects.all(),
        "programmes": Programme.objects.all(),
        "clubs": Club.objects.all()[:6],
        "promise_items": PromiseItem.objects.all(),
        "stats": StatCounter.objects.all(),
        "upcoming_events": Event.objects.filter(date__gte=timezone.now()).order_by("date")[:3],
        "latest_news": NewsPost.objects.filter(is_published=True).order_by("-published_at")[:3],
        "testimonials": Testimonial.objects.filter(is_active=True),
        "gallery_preview": GalleryImage.objects.all().order_by("-id")[:8],
    }
    return render(request, "home.html", context)


def about(request):
    context = {
        "meta_description": (
            "Learn about Carol & Kelly Joystar Academy's vision, mission, core values and "
            "school promise — Creating a Firm Foundation for every learner."
        ),
        "core_values": CoreValue.objects.all(),
        "promise_items": PromiseItem.objects.all(),
        "subject_areas": SubjectArea.objects.all()[:4],
    }
    return render(request, "about.html", context)