"""Songs app URL config"""

from rest_framework import routers

from .views import AlbumViewset


router = routers.DefaultRouter()

router.register(r'album', AlbumViewset, basename='album')

urlpatterns = router.urls
