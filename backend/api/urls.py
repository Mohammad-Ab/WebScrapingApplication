from django.urls import path,include
from .views import CorporationViewSet,EsgViewSet, UserViewSet
from rest_framework import routers

app_name = "api"

router = routers.SimpleRouter()
router.register('corps',CorporationViewSet, basename="corporation")
router.register('esgscore',EsgViewSet, basename="esgscore")
router.register('users',UserViewSet,basename="users")

urlpatterns = [
            path("",include(router.urls)),
        ]
