from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=25, help_text='Customer facing name of product')
    code = models.CharField(
        max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(help_text='Price of product in cents')

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)
