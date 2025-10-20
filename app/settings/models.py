from django.db import models

class Category(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категори'
        verbose_name_plural = 'Категорий'

class ModelProduct(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Название'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Модель'
        verbose_name_plural = 'Модели'

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='category_product',
        verbose_name='Категория продукта',
        blank=True, null=True
    )
    model = models.ForeignKey(
        ModelProduct,
        on_delete=models.SET_NULL,
        related_name='model_product',
        verbose_name='Модель продукта',
        blank=True, null=True
    )
    name = models.CharField(
        max_length=155,
        verbose_name='Название'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.CharField(
        max_length=15,
        verbose_name='Цена'
    )
    user = models.CharField(
        max_length=155,
        verbose_name='Владелец'
    )
    address = models.CharField(
        max_length=155,
        verbose_name='Адрес'
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name='Активен'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создание'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    

class ImageProduct(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product',
        verbose_name='Продукт'
    )
    images = models.ImageField(
        upload_to='product',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотография'