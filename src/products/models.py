from django.db import models
from django.urls import reverse

# Create your models here.
# everytime you modify models you need to run python manage.py makdemigrations and python manage.py migrate
class Product(models.Model):
    # Products need to inherit from models.Model to get features
    title       = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(max_digits=5,decimal_places=2)
    summary     = models.TextField(blank=False,null=False)
    featured    = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"my_id": self.id})
    