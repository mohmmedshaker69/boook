from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    state_choice = (
        ('avaliable', 'avaliable'),
        ('rented','rented'),
        ('sold', 'sold')
    )

    category = models.ForeignKey(Category, related_name='book', on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    rental_price_per_day = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    rental_period = models.IntegerField(null=True, blank=True)
    total_rental_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    photo_book = models.ImageField(upload_to='photos')
    photo_author = models.ImageField(upload_to='photos')
    active = models.BooleanField(default=True)
    status = models.CharField( max_length=100 , choices=state_choice)

  
    def total(self):
        self.total_rental_price = self.rental_price_per_day * self.rental_period
        self.save()  


    def __str__(self):
        return self.title