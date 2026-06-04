from django.urls import path

from .views import (
    SubscriptionPlanListCreateView,
    SubscriptionPlanDetailView,
    SubscriptionListCreateView,
    SubscriptionDetailView
)

urlpatterns = [

    path(
        "plans/",
        SubscriptionPlanListCreateView.as_view(),
        name="plan-list"
    ),

    path(
        "plans/<int:pk>/",
        SubscriptionPlanDetailView.as_view(),
        name="plan-detail"
    ),

    path(
        "subscriptions/",
        SubscriptionListCreateView.as_view(),
        name="subscription-list"
    ),

    path(
        "subscriptions/<int:pk>/",
        SubscriptionDetailView.as_view(),
        name="subscription-detail"
    ),
]