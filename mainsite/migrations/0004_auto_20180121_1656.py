# Generated by Django 2.0.1 on 2018-01-21 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20180121_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qatag',
            name='qa',
        ),
        migrations.RemoveField(
            model_name='qatag',
            name='tag',
        ),
        migrations.AddField(
            model_name='qa',
            name='tags',
            field=models.ManyToManyField(related_name='タッグ', to='mainsite.Tag'),
        ),
        migrations.DeleteModel(
            name='QaTag',
        ),
    ]