"""Movies app URL configuration"""

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'movies', views.MoviesViewset, basename='movie')
router.register(r'directors', views.DirectorViewset, basename='director')


print(router.urls)
urlpatterns = router.urls
