import io
import os

from django.conf import settings
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont


class Command(BaseCommand):
    help = "Generates a default 1200x630 Open Graph share image."

    def handle(self, *args, **options):
        img = Image.new("RGB", (1200, 630), "#0b6e4f")
        draw = ImageDraw.Draw(img)
        draw.rectangle([0, 0, 60, 630], fill="#b3122a")
        draw.rectangle([60, 0, 120, 630], fill="#16191b")
        draw.text((160, 260), "Carol and Kelly Joystar Academy", fill="white")
        draw.text((160, 320), "Creating a Firm Foundation", fill="white")

        out_dir = os.path.join(settings.BASE_DIR, "static", "img")
        os.makedirs(out_dir, exist_ok=True)
        img.save(os.path.join(out_dir, "og-default.jpg"), format="JPEG", quality=88)
        self.stdout.write(self.style.SUCCESS("Generated static/img/og-default.jpg"))