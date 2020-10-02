"""cancionero URL Configuration"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('canciones/', include(
        arg=('canciones.urls', 'canciones'),
        namespace='canciones'
    )),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
