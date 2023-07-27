from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}
class Category(models.Model):
    category_name = models.CharField(max_length=100,verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Каиегория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    photo = models.ImageField(upload_to="Image/", verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку', **NULLABLE)
    creation_date = models.DateField(verbose_name='Дата создания', **NULLABLE)
    last_modified_date = models.DateField(verbose_name='Дата последнего изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name} из категории {self.category}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('name',)
