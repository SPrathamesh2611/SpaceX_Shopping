# Generated by Django 4.2.1 on 2023-07-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceX_Shopping', '0006_cart_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product_id',
            field=models.CharField(default=1, max_length=50, verbose_name='user'),
            preserve_default=False,
        ),
    ]
