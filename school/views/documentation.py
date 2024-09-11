from drf_yasg import openapi
from drf_yasg.views import get_schema_view

...

schema_view = get_schema_view(
    openapi.Info(
        title="Documentation API",
        default_version="v1",
        description="School-API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)
