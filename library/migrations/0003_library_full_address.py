# Generated by Django 4.0.4 on 2022-04-16 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_rename_news_pic_library_library_pic_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='full_address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
