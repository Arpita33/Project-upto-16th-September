# Generated by Django 2.2.4 on 2019-09-15 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_spotreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='spotreview',
            name='rating',
            field=models.CharField(blank=True, default='0', max_length=5),
        ),
    ]