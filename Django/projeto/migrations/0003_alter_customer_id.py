# Generated by Django 4.1.7 on 2023-04-24 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_customer_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]