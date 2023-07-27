# Generated by Django 4.2.3 on 2023-07-27 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('category_description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Каиегория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='Image/', verbose_name='Превью')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена за покупку')),
                ('creation_date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('last_modified_date', models.DateField(blank=True, null=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ('name',),
            },
        ),
    ]