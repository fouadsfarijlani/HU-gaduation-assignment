# Generated by Django 3.2.3 on 2021-06-01 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material_Classifier', '0011_auto_20210531_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incentiveoffers',
            name='offer_image',
        ),
        migrations.AddField(
            model_name='incentiveoffers',
            name='offer_image_path',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
