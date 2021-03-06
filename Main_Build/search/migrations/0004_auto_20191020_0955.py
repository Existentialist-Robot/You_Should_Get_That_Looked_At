# Generated by Django 2.2.6 on 2019-10-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20191019_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metadata',
            name='active',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='author',
        ),
        migrations.RemoveField(
            model_name='metadata',
            name='thumb',
        ),
        migrations.AddField(
            model_name='metadata',
            name='month',
            field=models.CharField(default='January', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='x_coord',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='y_coord',
            field=models.CharField(default=2, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='year',
            field=models.CharField(default=3, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='metadata',
            name='z_coord',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
