# Generated by Django 4.2.1 on 2023-07-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SpaceX_Shopping', '0002_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='photo',
            field=models.CharField(default=0, max_length=50, verbose_name='photo'),
            preserve_default=False,
        ),
    ]
