# Generated by Django 4.0.1 on 2022-04-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_custom_user_email_alter_custom_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]