from django.urls import path
from rest_framework.routers import DefaultRouter

from app.settings.views import (
    CategoryAPIView, ProductAPI, CategoryCreateAPIView, ModelProductAPI,
    CategoryUpdateAPIView, CategoryDetailAPIView, CategoryDeleteAPIView, 
)

router = DefaultRouter()
router.register("product-api", ModelProductAPI, basename='model-product')
router.register("product", ProductAPI, basename='product')

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("category-create", CategoryCreateAPIView.as_view(), name='create-category'),
    path("category-update/<int:pk>/", CategoryUpdateAPIView.as_view(), name='category-update'),
    path("category-detail/<int:pk>/", CategoryDetailAPIView.as_view(), name='category-detail'),
    path("category-delete/<int:pk>/", CategoryDeleteAPIView.as_view(), name='category-delete'),
]


urlpatterns += router.urls