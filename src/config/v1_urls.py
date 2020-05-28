from django.urls import include, path


urlpatterns = [
    path("auth/", include("rest_framework.urls")),
    path("words/", include("words.urls")),
]
