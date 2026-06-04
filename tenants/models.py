from django.db import models


class Tenant(models.Model):

    company_name = models.CharField(max_length=150)
    company_email = models.EmailField()
    company_phone = models.CharField(max_length=15)
    company_address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tenants"

    def __str__(self):
        return self.company_name