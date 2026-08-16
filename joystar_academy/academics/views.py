from django.shortcuts import render

from core.models import Programme

from .models import SubjectArea, TeachingApproach


def academics(request):
    context = {
        "meta_description": (
            "Explore the Competency-Based Curriculum (CBC) at Carol & Kelly Joystar Academy, "
            "from Playgroup through Junior School, with small class sizes and modern ICT."
        ),
        "programmes": Programme.objects.exclude(stage=Programme.Stage.JUNIOR_SCHOOL),
        "subject_areas": SubjectArea.objects.all(),
        "teaching_approaches": TeachingApproach.objects.all(),
    }
    return render(request, "academics.html", context)