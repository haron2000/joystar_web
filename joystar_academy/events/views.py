from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Event, EventCategory


def event_list(request):
    events = Event.objects.select_related("category")

    query = request.GET.get("q", "").strip()
    category_slug = request.GET.get("category", "")
    month = request.GET.get("month", "")  # format YYYY-MM
    time_filter = request.GET.get("when", "")  # upcoming | past

    if query:
        events = events.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    if category_slug:
        events = events.filter(category__slug=category_slug)
    if month:
        try:
            year, mon = (int(part) for part in month.split("-"))
            events = events.filter(date__year=year, date__month=mon)
        except (ValueError, TypeError):
            pass

    now = timezone.now()
    if time_filter == "upcoming":
        events = events.filter(date__gte=now)
    elif time_filter == "past":
        events = events.filter(date__lt=now)

    month_options = (
        Event.objects.dates("date", "month", order="DESC") if Event.objects.exists() else []
    )

    context = {
        "meta_description": (
            "Upcoming and past events at Carol & Kelly Joystar Academy — open days, sports "
            "days, prize-giving, trips and more."
        ),
        "events": events.order_by("-date"),
        "categories": EventCategory.objects.all(),
        "month_options": month_options,
        "query": query,
        "active_category": category_slug,
        "active_month": month,
        "active_when": time_filter,
        "now": now,
    }
    return render(request, "events/list.html", context)


def event_detail(request, slug):
    event = get_object_or_404(Event.objects.select_related("category"), slug=slug)
    context = {
        "event": event,
        "meta_description": event.summary,
    }
    return render(request, "events/detail.html", context)