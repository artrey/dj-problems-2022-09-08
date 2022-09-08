import django_filters
from django_filters.rest_framework import FilterSet

from demo.models import Post


class PostFilterSet(FilterSet):
    u = django_filters.DateTimeFromToRangeFilter(field_name='updated_at')

    class Meta:
        model = Post
        fields = ['is_private', 'creator']
