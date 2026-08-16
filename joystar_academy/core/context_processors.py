from .models import SiteSettings


def site_settings(request):
    """Makes site-wide settings (contact info, socials, etc.) available in all templates."""
    return {"site": SiteSettings.load()}