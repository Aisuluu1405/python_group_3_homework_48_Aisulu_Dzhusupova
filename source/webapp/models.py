from django.db import models

CATEGORY_CHOICES = (
    ('other', 'Other'),
    ('clothes', 'Clothes'),
    ('shoes', 'Shoes'),
    ('accessories', 'Accessories'),
    ('beauty', 'Beauty'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Product name')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Description')
    category = models.CharField(max_length=30, null=False, blank=False, verbose_name='Category', default=CATEGORY_CHOICES[0][0],
                                choices=CATEGORY_CHOICES)
    count = models.FloatField(verbose_name='Count')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')


    def __str__(self):
        return self.name

# Create your models here.
