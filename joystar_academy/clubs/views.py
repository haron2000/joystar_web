from django.shortcuts import render

from .models import Club


def clubs(request):
    context = {
        "meta_description": (
            "Clubs and co-curricular activities at Carol & Kelly Joystar Academy: Coding & "
            "Robotics, Chess, Ballet, Music, Football, Arts, Junior Chef, Debate and Scouts."
        ),
        "clubs": Club.objects.filter(is_sport=False),
        "sports": Club.objects.filter(is_sport=True),
    }
    return render(request, "clubs.html", context)