from django.db import models


class ProductPrice(models.Model):
    """Sets date-based sale price of products"""
    code = models.CharField(
        max_length=10, help_text='Internal facing reference to product')
    price = models.PositiveIntegerField(
        help_text='Sale price of product in cents')
    price_start_date = models.DateField(help_text='First day at this price')
    price_end_date = models.DateField(
        help_text='Last day at this price', blank=True, null=True)

    def __str__(self):
        return 'Code: {}; Price: {}; Price start date: {}; Price end date: {}'.format(self.code, self.formatted_price, self.price_start_date, self.price_end_date)

    @property
    def formatted_price(self):
        return '${0:.2f}'.format(self.price / 100)
