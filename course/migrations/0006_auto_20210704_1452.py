# Generated by Django 3.2.5 on 2021-07-04 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_alter_product_full_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='little_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='full_description',
        ),
    ]