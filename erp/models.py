from email.policy import default
from re import T
from tabnanny import verbose
from django.db import models
from datetime import datetime

gender_choices = (
    ('male','Masculino'),
    ('female','Femenino'),
)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)

    def __str__(self):
        return 'Name: {}'.format(self.name)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['id']


class Client(models.Model):
    names = models.CharField(max_length=150, verbose_name='Names')
    surnames = models.CharField(max_length=150, verbose_name='Lastnames')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    birthday = models.DateField(default=datetime.now, verbose_name='Birth Date')
    address = models.CharField(max_length=150, null=True, blank=True, verbose_name='Address')
    sexo = models.CharField(max_length=10, choices=gender_choices, default='male', verbose_name='Gender')

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Sale Detail'
        verbose_name_plural = 'Sale Details'
        ordering = ['id']
