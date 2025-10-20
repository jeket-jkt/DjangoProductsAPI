from django.urls import path
from app.settings.views import CategoryAPIView, ModelProductAPI, ProductAPI, ProductDetailAPI

urlpatterns = [
    path("category", CategoryAPIView.as_view(), name='category'),
    path("model", ModelProductAPI.as_view(), name='model'),
    path("product", ProductAPI.as_view(), name='product'),
    path("product/<int:pk>/", ProductDetailAPI.as_view(), name='product_detail'),
]