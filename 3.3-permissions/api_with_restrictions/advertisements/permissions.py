from rest_framework.permissions import BasePermission

from advertisements.models import AdvertisementStatusChoices


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            if obj.status == AdvertisementStatusChoices.DRAFT:
                return request.user == obj.creator
            else:
                return True
        return request.user == obj.creator