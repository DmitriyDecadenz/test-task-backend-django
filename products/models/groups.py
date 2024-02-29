from django.db import models
from django.contrib.auth.models import User

users = User

class Group(models.Model):
    name = models.CharField('Название', max_length=255)
    members = models.ManyToManyField(
        User , 'groups_members', verbose_name='Участники группы',)
    product = models.ForeignKey('Product', models.CASCADE)
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группа'

    def __str__(self):
        return f'{self.name} ({self.pk})'
      
class Member(models.Model):
    group = models.ForeignKey(
        'Group', models.CASCADE, 'members_info',
    )
    employee = models.ForeignKey(
        'Employee', models.CASCADE, 'groups_info',
    )

    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'Участники групп'


    def __str__(self):
        return f'Employee {self.employee}'