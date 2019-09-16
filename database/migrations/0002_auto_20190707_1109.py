# Generated by Django 2.2.1 on 2019-07-07 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='userID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE'),
        ),
        migrations.AlterField(
            model_name='cityprofile',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE'),
        ),
        migrations.AlterField(
            model_name='guidetourinfo',
            name='guideID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE'),
        ),
        migrations.AlterField(
            model_name='profilegroup',
            name='userID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE'),
        ),
        migrations.AlterField(
            model_name='tourinfo',
            name='userID',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='RegLogin.PROFILE'),
        ),
        migrations.DeleteModel(
            name='PROFILE',
        ),
    ]