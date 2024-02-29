from django.db import models
from django.contrib.auth import get_user_model


class Lesson(models.Model):
    name = models.CharField('Название', max_length=255)
    video = models.URLField()
    product = models.ForeignKey('Product', models.CASCADE)
    student = models.ManyToManyField('Employee')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.name} ({self.pk})'