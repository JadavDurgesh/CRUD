# Generated by Django 4.1.3 on 2023-05-25 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_contact_us'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_product',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='contact_us',
        ),
        migrations.DeleteModel(
            name='Add_product',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
