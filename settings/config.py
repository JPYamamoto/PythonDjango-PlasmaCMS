from .models import Blog


def settings_dict(request):
    try:
        current_config_object = Blog.objects.last()
        current_config = {
            'SITE_NAME': current_config_object.name,
            'SITE_SLOGAN': current_config_object.slogan,
            'SITE_ICON': current_config_object.icon,
            'SITE_COVER': current_config_object.cover,
            'SITE_SN_FACEBOOK': current_config_object.sn_facebook,
            'SITE_SN_TWITTER': current_config_object.sn_twitter,
            'SITE_SN_MEDIUM': current_config_object.sn_medium,
            'SITE_SN_GITHUB': current_config_object.sn_github,
            'SITE_SN_LINKEDIN': current_config_object.sn_linkedin,
            'SITE_SN_YOUTUBE': current_config_object.sn_youtube,
            'SITE_SN_GOOGLE': current_config_object.sn_google,
        }
        return current_config
    except Exception:
        return {'SITE_NAME': 'Plasma'}
