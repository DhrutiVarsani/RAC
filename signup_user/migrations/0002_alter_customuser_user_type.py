# Generated by Django 3.2.7 on 2021-12-27 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('developer', 'developer'), ('client', 'client')], default='client', max_length=50),
        ),
    ]
