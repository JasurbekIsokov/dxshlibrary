# Generated by Django 4.0.4 on 2022-04-15 16:47

from django.db import migrations, models
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('open_year', models.IntegerField()),
                ('general_fund', models.IntegerField()),
                ('number_of_users', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('partnership_type', models.CharField(choices=[('yangi_bino', 'Yangi bino qurish'), ('tamirlash', 'Binoni tamirlash'), ('fondni_toldirish', "Fondni to'ldirish"), ('internet', 'internet'), ('moddiy_texnik', "Moddiy texnik ta'mirlash")], default='yangi_bino', max_length=50)),
                ('region', models.CharField(choices=[('andijon', 'Andijon viloyati'), ('buxoro', 'Buxoro viloyati'), ('fargona', "Farg'ona viloyati"), ('jizzax', 'Jizzax viloyati'), ('namangan', 'Namangan viloyati'), ('navoiy', 'Navoiy viloyati'), ('qoraqolpogiston', "Qoraqalpog'iston Respublikasi"), ('qashqadaryo', 'Qashqadaryo viloyati'), ('samarqand', 'Samarqand viloyati'), ('sirdaryo', 'Sirdaryo viloyati'), ('surxondaryo', 'Surxondaryo viloyati'), ('toshkent_viloyati', 'Toshkent viloyati'), ('toshkent_shahri', 'Toshkent shahri'), ('xorazm', 'Xorazm viloyati')], max_length=70)),
                ('news_pic', models.ImageField(upload_to=library.models.path_and_rename_library, verbose_name='Library Picture')),
            ],
        ),
    ]
