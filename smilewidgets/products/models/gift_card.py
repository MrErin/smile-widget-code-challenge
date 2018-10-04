from django.db import models


class GiftCard(models.Model):
    code = models.CharField(
        max_length=30, help_text='Internal facing reference to product')
    amount = models.PositiveIntegerField(
        help_text='Value of gift card in cents')
    date_start = models.DateField(help_text='First date card is valid')
    date_end = models.DateField(
        help_text='Last date card is valid', blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.code, self.formatted_amount)

    @property
    def formatted_amount(self):
        return '${0:.2f}'.format(self.amount / 100)
