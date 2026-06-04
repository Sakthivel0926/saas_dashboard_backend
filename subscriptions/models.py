from django.db import models
from tenants.models import Tenant


class SubscriptionPlan(models.Model):

    plan_name = models.CharField(max_length=100)

    description = models.TextField()

    monthly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    yearly_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    max_users = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        db_table = "subscription_plans"


class Subscription(models.Model):

    tenant = models.ForeignKey(
        Tenant,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    end_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default="ACTIVE"
    )

    class Meta:
        db_table = "subscriptions"