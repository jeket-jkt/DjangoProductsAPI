import django_filters
from app.settings.models import Product, ModelProduct

class ProductFilter(django_filters):
    category = django_filters
    field_name = 'category__name', lookup_expr=