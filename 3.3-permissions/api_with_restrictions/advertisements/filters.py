from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices

class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    date = DateFromToRangeFilter()
    status = ChoiceFilter(choices=(AdvertisementStatusChoices.OPEN, AdvertisementStatusChoices.CLOSED))

    class Meta:
        model = Advertisement
        fields = ['date', 'status']