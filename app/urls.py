from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import DriverViewSet, NationalityViewSet


router = DefaultRouter()
router.register(prefix=r"nationality", viewset=NationalityViewSet)
router.register(prefix=r"driver", viewset=DriverViewSet)


urlpatterns = [
    # Auth/Admin stuff
    path("admin/", admin.site.urls),
    path("api/v1", include("djoser.urls")),
    path("api/v1", include("djoser.urls.authtoken")),

    # URLS
    path("", include(router.urls))
]

