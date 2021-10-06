# Generated by Django 3.2.3 on 2021-05-30 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Material_Classifier', '0004_itemclassificationpicture_picture_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
    ]