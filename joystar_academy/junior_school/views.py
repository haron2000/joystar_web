from django.shortcuts import render

from .models import JuniorSchoolHighlight, LearningPathway


def junior_school(request):
    context = {
        "meta_description": (
            "Discover the Junior School pathway (Grade 7 - 8) at Carol & Kelly Joystar Academy, "
            "preparing learners for confident transition to Senior School."
        ),
        "highlights": JuniorSchoolHighlight.objects.all(),
        "pathways": LearningPathway.objects.all(),
    }
    return render(request, "junior_school.html", context)