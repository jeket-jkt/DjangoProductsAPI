from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from app.settings.models import Category, ModelProduct, ImageProduct, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ModelProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelProduct
        fields = ['id', 'name']


class ImageProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)
    images = Base64ImageField(required=False)

    class Meta:
        model = ImageProduct
        fields = ['id', 'images', 'image_url']

    def get_image_url(self, obj):
        request = self.context.get("request")
        if obj.images and hasattr(obj.images, "url"):
            return request.build_absolute_uri(obj.images.url) if request else obj.images.url
        return None


class ProductSerializer(serializers.ModelSerializer):
    images = ImageProductSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'model', 'name',
            'description', 'price', 'user', 'address',
            'is_active', 'created_at', 'images'
        ]