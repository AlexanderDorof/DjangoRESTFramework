from django.db import models


class Wonder(models.Model):
    CHOICES = (
        ('e', 'Exists'),
        ('d', 'Destroyed')
    )
    title = models.CharField(max_length=25, verbose_name='Название')
    creator = models.CharField(max_length=25, blank=True, verbose_name='Создатель')
    created = models.DateField(verbose_name='Дата постройки/создания')
    place = models.CharField(max_length=50, verbose_name='Расположение')
    current_status = models.CharField(max_length=25, choices=CHOICES, verbose_name='Статус')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Чудо'
        verbose_name_plural = 'Чудеса'
