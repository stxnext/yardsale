# Generated by Django 2.1.3 on 2018-11-25 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yardsale', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='django_classified.Item'),
        ),
    ]