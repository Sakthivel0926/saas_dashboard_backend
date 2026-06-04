from rest_framework import serializers

from .models import SubscriptionPlan, Subscription


class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="tenant.company_name", read_only=True)
    plan_name = serializers.CharField(source="plan.plan_name", read_only=True)

    class Meta:
        model = Subscription
        fields = [
            "id",
            "company_name",
            "plan_name",
            "start_date",
            "end_date",
            "status"
        ]