# Generated by Django 4.0.4 on 2022-05-27 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0004_location_remove_category_slug_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='squareImage',
        ),
    ]