# Generated by Django 2.2.4 on 2019-09-16 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_auto_20190915_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourinfo',
            name='dailyTravelTime',
        ),
        migrations.RemoveField(
            model_name='tourinfo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tourinfo',
            name='finished',
        ),
        migrations.RemoveField(
            model_name='tourinfo',
            name='groupID',
        ),
        migrations.AddField(
            model_name='tourinfo',
            name='context',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='tourinfo',
            name='endTime',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='tourinfo',
            name='startLocation',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='tourinfo',
            name='startTime',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='spotreview',
            name='rating',
            field=models.CharField(blank=True, default='-', max_length=5),
        ),
        migrations.AlterField(
            model_name='tourinfo',
            name='endDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='tourinfo',
            name='startDate',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
