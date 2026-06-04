from django.db import models

from tenants.models import Tenant
from subscriptions.models import Subscription


class Payment(models.Model):

    tenant = models.ForeignKey(Tenant,on_delete=models.CASCADE)

    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10,decimal_places=2)

    payment_method = models.CharField(max_length=50)

    transaction_id = models.CharField(max_length=100,unique=True)

    payment_status = models.CharField(max_length=50)

    paid_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payments"