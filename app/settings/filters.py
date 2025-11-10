import django_filters
from app.settings.models import Product, ModelProduct

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(
        field_name='category__name', lookup_expr='icontains', label='Категория'
    )
    model = django_filters.CharFilter(
        field_name='model__name', lookup_expr='icontains', label='Модель'
    )
    name = django_filters.CharFilter(
        field_name='name', lookup_expr='icontains', label='Title'
    )
    user = django_filters.CharFilter(
        field_name='user', lookup_expr='icontains', label='Owner'
    )
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['category', 'model', 'name', 'user', 'price_min', 'price_max', 'is_active']