# Generated by Django 3.2.7 on 2022-01-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup_user', '0003_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('developer', 'developer'), ('client', 'client')], default='client', max_length=50),
        ),
    ]
