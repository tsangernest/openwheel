from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from app.views import (CircuitViewSet, ConstructorStandingViewSet,
                       ConstructorViewSet, DriverStandingViewSet,
                       DriverViewSet, LapTimeViewSet, NationalityViewSet,
                       PitStopViewSet, QualifyingViewSet, RaceViewSet,
                       UploadView)

router = DefaultRouter()
router.register(prefix=r"nationality", viewset=NationalityViewSet)
router.register(prefix=r"driver", viewset=DriverViewSet)
router.register(prefix=r"constructor", viewset=ConstructorViewSet)
router.register(prefix=r"circuit", viewset=CircuitViewSet)
router.register(prefix=r"race", viewset=RaceViewSet)
router.register(prefix=r"qualifying", viewset=QualifyingViewSet)
router.register(prefix=r"laptime", viewset=LapTimeViewSet)
router.register(prefix=r"pitstop", viewset=PitStopViewSet)
router.register(prefix=r"driverstanding", viewset=DriverStandingViewSet)
router.register(prefix=r"constructorstanding", viewset=ConstructorStandingViewSet)


urlpatterns = [
    # Auth/Admin stuff
    path("admin/", admin.site.urls),
    path("api/v1", include("djoser.urls")),
    path("api/v1", include("djoser.urls.authtoken")),
    path(route="upload", view=UploadView.as_view()),

    # URLS
    path("", include(router.urls)),
]

