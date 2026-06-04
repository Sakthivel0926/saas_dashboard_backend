from django.urls import path

from .views import (
    TenantListCreateView,
    TenantDetailView
)

urlpatterns = [

    path(
        "tenants/",
        TenantListCreateView.as_view(),
        name="tenant-list"
    ),

    path(
        "tenants/<int:pk>/",
        TenantDetailView.as_view(),
        name="tenant-detail"
    ),
]