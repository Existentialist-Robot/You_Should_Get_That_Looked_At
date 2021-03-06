# Generated by Django 2.2.6 on 2019-10-19 22:06

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('search', '0002_contact_search'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Search',
            new_name='Profile',
        ),
        migrations.CreateModel(
            name='Metadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('thumb', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('author', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
