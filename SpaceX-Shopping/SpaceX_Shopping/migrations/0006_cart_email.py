# Generated by Django 4.2.1 on 2023-07-07 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceX_Shopping', '0005_cart_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='email',
            field=models.CharField(default=1, max_length=50, verbose_name='Email'),
            preserve_default=False,
        ),
    ]
