from django.db import models
from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField(blank=True, null=False)
    active = models.BooleanField(default = False)

    def get_absolute_url(self):
        # self is the url itself, its like a dictionary <int:id>/<int:listing> calling self.id gets the integer
        return reverse("article-detail", kwargs={"id": self.id})
