from django.db import models

# Create your models here.

class Phones(models.Model):
    model = models.CharField(max_length=30)
    make = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.model} {self.make} {self.price}"
