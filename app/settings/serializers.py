from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from app.settings.models import Category, ModelProduct, ImageProduct, Product
from django.apps import apps
from .models import Product, Review

app_models = apps.get_app_config('settings').get_models()
serializers_dict = {}

for model in app_models:
    meta = type('Meta', (), {'model': model, 'fields': '__all__'})
    serializer_class = type(f'{model.__name__}Serializer', (serializers.ModelSerializer,), {'Meta': meta})
    serializers_dict[model.__name__] = serializer_class


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category's name must be more than 3")
        return value


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

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Оценка должна быть от 1 до 5.")
        return value


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'average_rating', 'reviews']