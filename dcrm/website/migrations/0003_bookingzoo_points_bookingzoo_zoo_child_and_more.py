# Generated by Django 5.1.2 on 2024-11-18 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_bookinghotel_hotel_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingzoo',
            name='points',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bookingzoo',
            name='zoo_child',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bookingzoo',
            name='zoo_adult',
            field=models.IntegerField(default=0),
        ),
    ]
