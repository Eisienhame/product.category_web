# Generated by Django 4.2 on 2023-05-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(max_length=400, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('description', models.CharField(blank=True, max_length=400, null=True, verbose_name='Описание')),
                ('preview_image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение (превью)')),
                ('category', models.CharField(max_length=150, verbose_name='Категория')),
                ('price', models.IntegerField(verbose_name='Цена за покупку')),
                ('date_of_creation', models.DateTimeField(verbose_name='Дата создания')),
                ('Last_modified_date', models.DateTimeField(verbose_name='Дата последнего изменения')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'студенты',
                'ordering': ('name',),
            },
        ),
    ]
