from rest_framework import viewsets, mixins, filters
from rest_framework.generics import ListAPIView
from django.apps import apps
from app.settings.models import Category, ModelProduct, Product
from app.settings.serializers import CategorySerializer, ModelProductSerializer, ProductSerializer
from .serializers import serializers_dict, ReviewSerializer
from .models import Review
from app.settings.pagination import StandartPagination


app_models = apps.get_app_config('settings').get_models()
viewsets_dict = {}

for model in app_models:
    serializer_class = serializers_dict[model.__name__]
    viewset_class = type(
        f'{model.__name__}ViewSet',
        (viewsets.ModelViewSet,),
        {
            'queryset': model.objects.all(),
            'serializer_class': serializer_class
        }
    )
    viewsets_dict[model.__name__] = viewset_class


class CategoryViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = StandartPagination


class ModelProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer
    pagination_class = StandartPagination

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'name']


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartPagination


class ReviewViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs.get("product_id")
        if product_id:
            return Review.objects.filter(product_id=product_id)
        return Review.objects.all()