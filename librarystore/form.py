# project/urls.py
from django.conf import settings
from django.conf.urls.static import static
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


urlpatterns = [
    # other url patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
