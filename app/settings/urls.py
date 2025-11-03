from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet, ProductViewSet, ModelProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'modelproducts', ModelProductViewSet, basename='modelproducts')

review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
review_detail = ReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('products/<int:product_id>/reviews/', review_list, name='review-list'),
    path('products/<int:product_id>/reviews/<int:pk>/', review_detail, name='review-detail'),

    path('', include(router.urls)),
]