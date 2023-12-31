# Generated by Django 4.2.4 on 2023-08-22 13:04

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('main', '0002_alter_location_l_description_alter_location_l_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
