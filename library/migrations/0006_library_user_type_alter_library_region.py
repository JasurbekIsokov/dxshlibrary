# Generated by Django 4.0.4 on 2022-04-17 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_library_user_alter_library_partnership_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='user_type',
            field=models.CharField(default='library', max_length=15),
        ),
        migrations.AlterField(
            model_name='library',
            name='region',
            field=models.CharField(choices=[('Andijon', 'Andijon viloyati'), ('Buxoro', 'Buxoro viloyati'), ("Farg'ona", "Farg'ona viloyati"), ('Jizzax', 'Jizzax viloyati'), ('Namangan', 'Namangan viloyati'), ('Navoiy', 'Navoiy viloyati'), ("Qoraqolpog'iston", "Qoraqalpog'iston Respublikasi"), ('Qashqadaryo', 'Qashqadaryo viloyati'), ('Samarqand', 'Samarqand viloyati'), ('Sirdaryo', 'Sirdaryo viloyati'), ('Surxondaryo', 'Surxondaryo viloyati'), ('Toshkent viloyati', 'Toshkent viloyati'), ('Toshkent shahri', 'Toshkent shahri'), ('Xorazm', 'Xorazm viloyati')], max_length=70),
        ),
    ]
