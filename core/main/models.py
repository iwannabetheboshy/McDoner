from django.db import models

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50)
    phone = models.CharField('Номер телефона', max_length=20)
    question = models.TextField('Запрос',blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Завяка'
        verbose_name_plural = 'Заявки'
