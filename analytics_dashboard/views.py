from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from tenants.models import Tenant
from subscriptions.models import Subscription


class DashboardAnalyticsView(APIView):

    def get(self, request):

        data = {
            "total_users": User.objects.count(),
            "total_tenants": Tenant.objects.count(),
            "active_subscriptions": Subscription.objects.filter(
                status="ACTIVE"
            ).count(),
        }

        return Response(data)