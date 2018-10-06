from django.db import models


class Product(models.Model):
    """Creates a new widget"""
    name = models.CharField(
        max_length=25, help_text='Customer facing name of product')
    code = models.CharField(
        max_length=10, help_text='Internal facing reference to product')
    # removing the "price" field from this model because prices are now managed on the ProductPrice table.

    def __str__(self):
        return '{} - {}'.format(self.name, self.code)
