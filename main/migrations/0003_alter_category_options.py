# Generated by Django 3.2.15 on 2022-10-03 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
    ]
