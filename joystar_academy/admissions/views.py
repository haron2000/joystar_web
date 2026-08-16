from django.contrib import messages
from django.shortcuts import redirect, render

from core.models import Programme

from .models import AdmissionInquiry, AdmissionStep, RequiredDocument


def admissions(request):
    if request.method == "POST":
        request_type = request.POST.get("request_type", AdmissionInquiry.RequestType.APPLY)
        parent_name = request.POST.get("parent_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()

        if parent_name and email and phone:
            AdmissionInquiry.objects.create(
                request_type=request_type,
                parent_name=parent_name,
                email=email,
                phone=phone,
                child_name=request.POST.get("child_name", "").strip(),
                desired_programme=request.POST.get("desired_programme", "").strip(),
                preferred_date=request.POST.get("preferred_date") or None,
                message=request.POST.get("message", "").strip(),
            )
            messages.success(
                request,
                "Thank you! Your request has been received — our admissions team will contact you soon.",
            )
            return redirect("admissions:admissions")
        messages.error(request, "Please fill in your name, email and phone number.")

    context = {
        "meta_description": (
            "Admissions at Carol & Kelly Joystar Academy: how to apply, book a school visit, "
            "and required documents for Playgroup through Junior School."
        ),
        "steps": AdmissionStep.objects.all(),
        "documents": RequiredDocument.objects.all(),
        "programmes": Programme.objects.all(),
    }
    return render(request, "admissions.html", context)