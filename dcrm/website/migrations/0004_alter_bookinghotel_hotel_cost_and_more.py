# Generated by Django 5.1.2 on 2024-11-18 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_bookingzoo_points_bookingzoo_zoo_child_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinghotel',
            name='Hotel_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookingzoo',
            name='zoo_cost',
            field=models.IntegerField(default=10),
        ),
    ]
