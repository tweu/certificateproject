# Generated by Django 3.2.5 on 2021-07-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_product_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='little_description',
        ),
        migrations.AddField(
            model_name='product',
            name='full_description',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
