# Generated by Django 5.0.3 on 2024-04-18 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='Medicine_ID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
