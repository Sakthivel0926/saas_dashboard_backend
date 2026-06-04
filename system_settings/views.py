from rest_framework import generics

from .models import SystemSetting
from .serializers import SystemSettingSerializer


class SystemSettingListCreateView(
    generics.ListCreateAPIView
):

    queryset = SystemSetting.objects.all()
    serializer_class = SystemSettingSerializer


class SystemSettingDetailView(
    generics.RetrieveUpdateDestroyAPIView
):

    queryset = SystemSetting.objects.all()
    serializer_class = SystemSettingSerializer