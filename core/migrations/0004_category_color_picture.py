# Generated by Django 3.2.7 on 2022-01-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color_picture',
            field=models.ImageField(blank=True, upload_to='Images'),
        ),
    ]
