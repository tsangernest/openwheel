from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter

from app.views import (CircuitViewSet,
                       ConstructorViewSet,
                       DriverViewSet,
                       LapTimeViewSet,
                       NationalityViewSet,
                       PitStopViewSet,
                       RaceViewSet,
                       QualifyingViewSet)


router = DefaultRouter()
router.register(prefix=r"nationality", viewset=NationalityViewSet)
router.register(prefix=r"driver", viewset=DriverViewSet)
router.register(prefix=r"constructor", viewset=ConstructorViewSet)
router.register(prefix=r"circuit", viewset=CircuitViewSet)
router.register(prefix=r"race", viewset=RaceViewSet)
router.register(prefix=r"qualifying", viewset=QualifyingViewSet)
router.register(prefix=r"laptime", viewset=LapTimeViewSet)
router.register(prefix=r"pitstop", viewset=PitStopViewSet)


urlpatterns = [
    # Auth/Admin stuff
    path("admin/", admin.site.urls),
    path("api/v1", include("djoser.urls")),
    path("api/v1", include("djoser.urls.authtoken")),

    # URLS
    path("", include(router.urls))
]

