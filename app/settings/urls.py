from django.urls import path, include
from app.settings.views import CategoryAPIView, ModelProductAPI, ProductAPI, ProductDetailAPI, CategoryDeleteAPIView, \
    ModelProductViewSet
from rest_framework.routers import DefaultRouter
from .views import viewsets_dict, ReviewViewSet, ModelProductViewSet, ProductViewSet

router = DefaultRouter()

review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
review_detail = ReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

router.register(r'products', ProductViewSet, basename='products')
router.register(r'modelproducts', ModelProductViewSet, basename='modelproducts')

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("model", ModelProductAPI.as_view(), name='model'),
    path("product", ProductAPI.as_view(), name='product'),
    path("product/<int:pk>/", ProductDetailAPI.as_view(), name='product_detail'),
    path("category-delete", CategoryDeleteAPIView.as_view(), name='category_delete'),
    path('products/<int:product_id>/reviews/', review_list, name='review-list'),
    path('products/<int:product_id>/reviews/<int:pk>/', review_detail, name='review-detail'),
    path('', include(router.urls)),
]

INSTALLED_APPS = [
    ...,
    'rest_framework',
]