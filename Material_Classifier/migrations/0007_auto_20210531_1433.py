# Generated by Django 3.2.3 on 2021-05-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Material_Classifier', '0006_itemclassificationresults_is_correct'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemclassificationresults',
            name='marked_for_futur_training',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='itemclassificationresults',
            name='rectified_label',
            field=models.CharField(default='N/A', max_length=150),
        ),
    ]