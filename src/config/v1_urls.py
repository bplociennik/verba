from django.urls import include, path


urlpatterns = [
    path("drf-auth/", include("rest_framework.urls")),
    path("auth/", include("dj_rest_auth.urls")),
    path("words/", include("words.urls")),
]
