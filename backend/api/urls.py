from django.urls import path,include
from .views import CorporationViewSet,EsgScoreViewSet
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('corps',CorporationViewSet, basename="corporation")
router.register('esgscore',EsgScoreViewSet, basename="esgscore")

urlpatterns = [
            path("",include(router.urls)),
        ]
