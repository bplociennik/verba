from rest_framework import routers

from .views import WordViewSet


router = routers.DefaultRouter()
router.register("", WordViewSet, basename="word")
urlpatterns = router.urls
