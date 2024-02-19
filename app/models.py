from django.db import models

# Create your models here.
class Product(models.Model):
    item_name = models.CharField(max_length=255)
    item_desc = models.CharField(max_length=255)
    item_price = models.FloatField()
    item_image = models.ImageField(upload_to='itemImg')
    
    def _str_(self):
        return self.item_name