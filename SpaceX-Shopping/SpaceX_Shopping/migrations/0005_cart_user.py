# Generated by Django 4.2.1 on 2023-07-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceX_Shopping', '0004_alter_cart_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.CharField(default=1, max_length=50, verbose_name='user'),
            preserve_default=False,
        ),
    ]
