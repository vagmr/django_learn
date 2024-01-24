from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Books(models.Model):
    bid = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=30, unique=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(
        validators=[MinValueValidator(1, message="Pages must be greater than 0")])
    price = models.FloatField(null=True, default=19.9)

    def __str__(self):
        return f"{self.title} by {self.author} %d" % (self.bid)
