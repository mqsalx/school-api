from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

app_name = "admin"

urlpatterns = [

    path("", include("school.urls.setup")),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
