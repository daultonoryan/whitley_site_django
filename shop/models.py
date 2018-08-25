from django.db import models
import uuid

class Shop_Item(models.Model):
    title = models.CharField(max_length=100, blank=True)
    price = models.IntegerField(blank=True)
    url = models.CharField(default="for_sale/", max_length=100 )
    description = models.CharField(max_length=1000, blank=True)
    image_main = models.ImageField(upload_to="static/for_sale", )
    product_url = models.CharField(default=uuid.uuid4(), max_length=100, unique=True)

    def __str__(self):
        return self.title
