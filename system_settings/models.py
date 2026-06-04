from django.db import models


class SystemSetting(models.Model):

    site_name = models.CharField(
        max_length=150
    )

    support_email = models.EmailField()

    maintenance_mode = models.BooleanField(
        default=False
    )

    timezone = models.CharField(
        max_length=100
    )

    class Meta:
        db_table = "system_settings"