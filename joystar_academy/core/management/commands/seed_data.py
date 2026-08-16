from datetime import timedelta

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils import timezone
from PIL import Image, ImageDraw
import io

from academics.models import SubjectArea, TeachingApproach
from admissions.models import AdmissionStep, RequiredDocument
from clubs.models import Club
from core.models import (
    CoreValue, HeroSlide, Programme, PromiseItem,
    SiteSettings, StatCounter, Testimonial, WhyChooseUsItem,
)
from events.models import Event, EventCategory
from gallery.models import GalleryCategory, GalleryImage
from junior_school.models import JuniorSchoolHighlight, LearningPathway
from news.models import NewsCategory, NewsPost


def make_placeholder_image(color, label):
    """Generates a simple flat-color placeholder image (no internet needed)."""
    img = Image.new("RGB", (1200, 800), color)
    draw = ImageDraw.Draw(img)
    draw.text((40, 40), label, fill="white")
    buffer = io.BytesIO()
    img.save(buffer, format="JPEG", quality=85)
    return ContentFile(buffer.getvalue(), name=f"{label.lower().replace(' ', '_')}.jpg")


class Command(BaseCommand):
    help = "Seeds the database with Carol & Kelly Joystar Academy demo content."

    def handle(self, *args, **options):
        # --- Site settings ---
        settings_obj = SiteSettings.load()
        settings_obj.email = "info@joystaracademy.ac.ke"
        settings_obj.save()
        self.stdout.write(self.style.SUCCESS("Site settings updated."))

        # --- Core values ---
        for i, name in enumerate([
            "Fear of God", "Integrity", "Discipline", "Responsibility",
            "Excellence", "Creativity", "Teamwork", "Respect", "Accountability",
        ]):
            CoreValue.objects.get_or_create(name=name, defaults={"order": i})

        # --- Promise items ---
        for i, text in enumerate([
            "We teach with care.", "We inspire curiosity.", "We build confidence.",
            "We nurture character.", "We unlock every child's potential.",
        ]):
            PromiseItem.objects.get_or_create(text=text, defaults={"order": i})

        # --- Hero slides (generated placeholder images) ---
        hero_colors = [
            ("#0b6e4f", "Learning Together"),
            ("#b3122a", "Building Confidence"),
            ("#16191b", "Coding & Robotics"),
            ("#c9a24b", "Sports & Talent"),
        ]
        for i, (color, caption) in enumerate(hero_colors):
            if not HeroSlide.objects.filter(caption=caption).exists():
                slide = HeroSlide(caption=caption, order=i)
                slide.image.save(f"hero_{i}.jpg", make_placeholder_image(color, caption), save=False)
                slide.save()

        # --- Why Choose Us ---
        why_items = [
            ("Competency-Based Curriculum", "CBC-aligned learning from Playgroup to Junior School."),
            ("Qualified Teachers", "Experienced, caring and passionate educators."),
            ("Small Class Sizes", "Individual attention for every learner."),
            ("Modern ICT", "Well-equipped computer labs and digital literacy."),
            ("Coding & Robotics", "Hands-on STEM skills from an early age."),
            ("Safe Environment", "A secure, nurturing campus for every child."),
        ]
        for i, (title, desc) in enumerate(why_items):
            WhyChooseUsItem.objects.get_or_create(title=title, defaults={"description": desc, "order": i})

        # --- Programmes ---
        programmes = [
            ("Playgroup", Programme.Stage.EARLY_YEARS, "3-4 years"),
            ("PP1", Programme.Stage.EARLY_YEARS, "4-5 years"),
            ("PP2", Programme.Stage.EARLY_YEARS, "5-6 years"),
            ("Grade 1", Programme.Stage.LOWER_PRIMARY, "6-7 years"),
            ("Grade 2", Programme.Stage.LOWER_PRIMARY, "7-8 years"),
            ("Grade 3", Programme.Stage.LOWER_PRIMARY, "8-9 years"),
            ("Grade 4", Programme.Stage.UPPER_PRIMARY, "9-10 years"),
            ("Grade 5", Programme.Stage.UPPER_PRIMARY, "10-11 years"),
            ("Grade 6", Programme.Stage.UPPER_PRIMARY, "11-12 years"),
            ("Grade 7", Programme.Stage.JUNIOR_SCHOOL, "12-13 years"),
            ("Grade 8", Programme.Stage.JUNIOR_SCHOOL, "13-14 years"),
        ]
        for i, (name, stage, age) in enumerate(programmes):
            Programme.objects.get_or_create(name=name, defaults={"stage": stage, "age_range": age, "order": i})

        # --- Stat counters ---
        stats = [("Years of Excellence", 10), ("Happy Learners", 500), ("Clubs & Activities", 9), ("Qualified Teachers", 30)]
        for i, (label, value) in enumerate(stats):
            StatCounter.objects.get_or_create(label=label, defaults={"value": value, "order": i})

        # --- Testimonials ---
        testimonials = [
            ("Mrs. Wanjiru", "Parent, Grade 3", "My daughter has grown so much in confidence since joining. The teachers truly care."),
            ("Mr. Otieno", "Parent, PP2", "A warm, safe environment where my son loves going to school every day."),
            ("Faith N.", "Grade 6 Learner", "I love robotics club! My teachers always help me learn new things."),
        ]
        for i, (name, role, quote) in enumerate(testimonials):
            Testimonial.objects.get_or_create(author_name=name, defaults={"role": role, "quote": quote, "order": i})

        # --- Clubs & Sports ---
        clubs = [
            ("Coding & Robotics", False), ("Chess Club", False), ("Ballet Club", False),
            ("Music Club", False), ("Arts Club", False), ("Junior Chef", False),
            ("Debate", False), ("Scouts", False), ("Football", True),
        ]
        for i, (name, is_sport) in enumerate(clubs):
            Club.objects.get_or_create(name=name, defaults={"is_sport": is_sport, "order": i})

        # --- Academics ---
        for i, name in enumerate(["Literacy", "Mathematics", "Creative Arts", "ICT"]):
            SubjectArea.objects.get_or_create(name=name, defaults={"order": i})
        for i, title in enumerate(["Experiential Learning", "Individual Attention", "Small Class Sizes"]):
            TeachingApproach.objects.get_or_create(title=title, defaults={"order": i})

        # --- Junior School ---
        for i, title in enumerate(["Subject Specialisation", "Career Pathways", "Leadership"]):
            JuniorSchoolHighlight.objects.get_or_create(title=title, defaults={"order": i})
        for i, name in enumerate(["STEM Pathway", "Arts & Sports Pathway", "Social Sciences Pathway"]):
            LearningPathway.objects.get_or_create(name=name, defaults={"order": i})

        # --- Admissions ---
        steps = [
            (1, "Book a Visit", "Tour the campus with our admissions team."),
            (2, "Submit Application", "Fill in the form with learner details."),
            (3, "Assessment", "A short placement conversation."),
            (4, "Enrollment", "Welcome to the Joystar family."),
        ]
        for num, title, desc in steps:
            AdmissionStep.objects.get_or_create(step_number=num, defaults={"title": title, "description": desc})
        for i, doc in enumerate(["Birth certificate copy", "Passport photos", "Previous school report"]):
            RequiredDocument.objects.get_or_create(name=doc, defaults={"order": i})

        # --- Events ---
        cat_sports, _ = EventCategory.objects.get_or_create(name="Sports")
        cat_academic, _ = EventCategory.objects.get_or_create(name="Academics")
        now = timezone.now()
        events = [
            ("Inter-house Sports Day", cat_sports, now + timedelta(days=10), "Academy grounds", "A full day of athletics and team games across all four houses."),
            ("Open Day", cat_academic, now + timedelta(days=18), "Main hall", "Tour the campus and meet our teachers."),
            ("Science & Robotics Fair", cat_academic, now - timedelta(days=20), "Main hall", "Grade 5-8 project showcase."),
        ]
        for title, cat, date, venue, summary in events:
            Event.objects.get_or_create(title=title, defaults={
                "category": cat, "date": date, "venue": venue, "summary": summary, "description": summary,
            })

        # --- News ---
        cat_news_academic, _ = NewsCategory.objects.get_or_create(name="Academics")
        posts = [
            ("Term 2 Results Announced", cat_news_academic, "Our learners recorded outstanding results this term.", "We are proud to share that Carol & Kelly Joystar Academy learners recorded outstanding results this term, with strong performance across mathematics, literacy and the sciences."),
        ]
        for title, cat, excerpt, body in posts:
            NewsPost.objects.get_or_create(title=title, defaults={
                "category": cat, "excerpt": excerpt, "body": body, "published_at": now,
            })

        # --- Gallery categories ---
        for i, name in enumerate(["Sports", "Academics", "Trips", "Robotics", "Arts", "Music", "Events"]):
            GalleryCategory.objects.get_or_create(name=name, defaults={"slug": name.lower(), "order": i})

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully!"))