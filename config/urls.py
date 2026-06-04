from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/", include("accounts.urls")),
    path("api/", include("tenants.urls")),
    path("api/", include("subscriptions.urls")),
    path("api/", include("payments.urls")),
    path("api/", include("notifications.urls")),
    path("api/", include("system_settings.urls")),
    path("api/analytics/", include("analytics_dashboard.urls")),
]