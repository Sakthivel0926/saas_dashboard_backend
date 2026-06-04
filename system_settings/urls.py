from django.urls import path

from .views import (
    SystemSettingListCreateView,
    SystemSettingDetailView
)

urlpatterns = [

    path(
        "settings/",
        SystemSettingListCreateView.as_view(),
        name="setting-list"
    ),

    path(
        "settings/<int:pk>/",
        SystemSettingDetailView.as_view(),
        name="setting-detail"
    ),
]