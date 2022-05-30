# Generated by Django 4.0.4 on 2022-05-30 11:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0003_alter_image_squareimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='squareImage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='default_square_jpg', force_format=None, keep_meta=True, quality=75, size=(1000, 1000), upload_to='square'),
        ),
    ]