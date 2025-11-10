from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView,\
RetrieveAPIView, DestroyAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, filters
from django_filters.rest_framework import DjangoFilterBackend

from app.settings.models import Category, ModelProduct, Product
from app.settings.serilizers import CategorySerializer, ModelProductSerializer,\
ProductSerializer
from app.settings.pagination import StandartPagination
from app.settings.filters import ProductFilter

class CategoryAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ModelProductAPI(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = ModelProduct.objects.all()
    serializer_class = ModelProductSerializer
    pagination_class = StandartPagination

class ProductAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartPagination

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['name', 'description', "category__name", "model__name", "user"]
    ordering_fields = ['price', 'created_at']