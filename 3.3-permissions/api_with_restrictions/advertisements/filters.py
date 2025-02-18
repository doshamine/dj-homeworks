from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter(field_name='created_at')
    status = ChoiceFilter(
        field_name='status',
        choices=(
            AdvertisementStatusChoices.OPEN,
            AdvertisementStatusChoices.CLOSED,
            AdvertisementStatusChoices.DRAFT
        )
    )

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status', 'creator']