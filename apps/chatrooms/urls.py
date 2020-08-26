from django.urls import include, path
from rest_framework import routers


from apps.chatrooms.views import RoomViewSet


router = routers.DefaultRouter()

router.register("rooms", RoomViewSet, basename="rooms-view-set")


urlpatterns = [
    path("", include(router.urls))
]