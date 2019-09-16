# Generated by Django 2.2.4 on 2019-09-15 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RegLogin', '0002_auto_20190708_1358'),
        ('database', '0008_spot_holiday'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPOTREVIEW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(blank=True, default='-', max_length=5)),
                ('review', models.CharField(blank=True, default='-', max_length=300)),
                ('spotID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.SPOT')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE')),
            ],
        ),
    ]
