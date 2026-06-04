from rest_framework import generics

from .models import SubscriptionPlan, Subscription
from .serializers import (
    SubscriptionPlanSerializer,
    SubscriptionSerializer
)


class SubscriptionPlanListCreateView(
    generics.ListCreateAPIView
):

    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer


class SubscriptionPlanDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer


class SubscriptionListCreateView(
    generics.ListCreateAPIView
):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class SubscriptionDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer