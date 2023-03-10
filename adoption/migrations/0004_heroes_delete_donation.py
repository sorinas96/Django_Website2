# Generated by Django 4.1.7 on 2023-03-05 16:42

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adoption', '0003_pets_poster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heroes',
            fields=[
                ('pets_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='adoption.pets')),
                ('personality', models.CharField(default='', max_length=200)),
                ('job_title', models.CharField(default='', max_length=200)),
                ('favorite_food', models.CharField(default='', max_length=200)),
                ('weight', models.IntegerField(validators=[django.core.validators.MaxValueValidator(19)])),
            ],
            bases=('adoption.pets',),
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
