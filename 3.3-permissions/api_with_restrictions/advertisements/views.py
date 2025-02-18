from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['created_at', 'status', 'creator']

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        elif self.action in ["retrieve", "list", "update", "partial_update", "destroy"]:
            return [IsOwnerOrReadOnly()]
        return []
