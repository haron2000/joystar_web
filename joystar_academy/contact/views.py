from django.contrib import messages
from django.shortcuts import redirect, render

from .models import ContactMessage


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, phone=phone, subject=subject, message=message
            )
            messages.success(
                request,
                "Thank you for reaching out! We've received your message and will respond shortly.",
            )
            return redirect("contact:contact")
        messages.error(request, "Please fill in your name, email and message before sending.")

    context = {
        "meta_description": (
            "Get in touch with Carol & Kelly Joystar Academy, Umoja 1 Q46, Nairobi. "
            "Call 0700347587 or send us a message."
        ),
    }
    return render(request, "contact.html", context)