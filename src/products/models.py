from django.db import models

# Create your models here.
# everytime you modify models you need to run python manage.py makdemigrations and python manage.py migrate
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True,null=True)
    price       = models.DecimalField(max_digits=4,decimal_places=2)
    summary     = models.TextField(blank=False,null=False)
    featured    = models.BooleanField(default=False)