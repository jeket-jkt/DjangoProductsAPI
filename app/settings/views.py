from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView
from app.settings.models import Category, ModelProduct, Product
from app.settings.serializers import CategorySerializer, ModelProductSerializer, ProductSerializer
from rest_framework import viewsets, mixins
from django.apps import apps
from .serializers import serializers_dict, ReviewSerializer
from .models import Review

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


class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ModelProductAPI(ListAPIView):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer


class ProductAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

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