from .models import *
from django_filters import FilterSet


class FoodFilter(FilterSet):
    class Meta:
        model = Food
        fields = {
            'price': ['lt', 'gt'],
            'category': ['exact']
        }