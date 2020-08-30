from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.DecimalField(max_digits=5, decimal_places=0)
    picture = models.CharField(
        default='https://thumbs.dreamstime.com/b/no-thumbnail-image-placeholder-forums-blogs-websites-148010362.jpg',
        max_length=255)


class Image(models.Model):
    url = models.CharField(
        default='https://thumbs.dreamstime.com/b/no-thumbnail-image-placeholder-forums-blogs-websites-148010362.jpg',
        max_length=255)
    upload_to = models.ImageField()


class ProductImage(models.Model):
    all_product_names = [(product.id, product.name) for product in Product.objects.all()]
    selected_product = models.IntegerField(choices=all_product_names, max_length=255, null=True, blank=True)
    all_product_images = [(image.id, image.url) for image in Image.objects.all()]
    selected_image = models.IntegerField(choices=all_product_images, max_length=255, null=True,
                                         blank=True)
