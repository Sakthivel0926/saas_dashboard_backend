from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.models import User
from tenants.models import Tenant
from subscriptions.models import Subscription


class DashboardAnalyticsView(APIView):

    def get(self, request):

        total_users = User.objects.count()

        total_tenants = Tenant.objects.count()

        active_subscriptions = Subscription.objects.filter(
            status="ACTIVE"
        )

        total_active_subscriptions = active_subscriptions.count()

        total_revenue = 0

        for subscription in active_subscriptions:
            total_revenue += subscription.plan.monthly_price

        return Response({
            "total_users": total_users,
            "total_tenants": total_tenants,
            "active_subscriptions": total_active_subscriptions,
            "total_revenue": total_revenue
        })