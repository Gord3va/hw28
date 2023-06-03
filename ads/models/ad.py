
from django.db import models

from ads.models.category import Category
from users.models import User


class Ad(models.Model):
    name = models.CharField(max_length=100)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=2000)
    # address = models.CharField(max_length=100)
    is_published = models.BooleanField(default="None")
    image = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return self.name