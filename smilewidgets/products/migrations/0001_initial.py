# Generated by Django 2.0.7 on 2018-10-06 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Internal facing reference to product', max_length=30)),
                ('amount', models.PositiveIntegerField(help_text='Value of gift card in cents')),
                ('date_start', models.DateField(help_text='First date card is valid')),
                ('date_end', models.DateField(blank=True, help_text='Last date card is valid', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Customer facing name of product', max_length=25)),
                ('code', models.CharField(help_text='Internal facing reference to product', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Internal facing reference to product', max_length=10)),
                ('price', models.PositiveIntegerField(help_text='Sale price of product in cents')),
                ('price_start_date', models.DateField(help_text='First day at this price')),
                ('price_end_date', models.DateField(blank=True, help_text='Last day at this price', null=True)),
            ],
        ),
    ]
