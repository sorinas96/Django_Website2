# Generated by Django 4.1.7 on 2023-02-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]