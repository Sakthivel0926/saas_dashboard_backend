from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):

    company_name = serializers.CharField(source="tenant.company_name", read_only=True)
    plan_name = serializers.CharField(source="subscription.plan.plan_name", read_only=True)

    class Meta:
        model = Payment
        fields = [
            "id",
            "company_name",
            "plan_name",
            "amount",
            "payment_method",
            "transaction_id",
            "payment_status",
            "paid_at"
        ]