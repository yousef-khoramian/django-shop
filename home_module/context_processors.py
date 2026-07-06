from home_module.models import SiteSettings

def site_settings(request):
    return {
        'site_setting':SiteSettings.objects.filter(is_active=True).first()
    }