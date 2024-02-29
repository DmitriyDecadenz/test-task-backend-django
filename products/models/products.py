from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    author = models.CharField(max_length=255)
    students = models.ManyToManyField(
        User, verbose_name='Студенты продукта'
        )
    min_members = models.PositiveIntegerField()
    max_members = models.PositiveIntegerField()
    price = models.PositiveBigIntegerField()
    date_start = models.DateField()
    date_end = models.DateField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('name', 'id',)

    def __str__(self):
        return f'{self.name} ({self.pk})'
      
class Employee(models.Model):
    product = models.ForeignKey(
        'Product', models.CASCADE, 
    )
    user = models.ForeignKey(
        User, models.CASCADE,
    )
    class Meta:
        verbose_name = 'Участник Продукта'
        verbose_name_plural = 'Участник Продукта'

    def __str__(self):
        return f'Members {self.product} {self.user}'