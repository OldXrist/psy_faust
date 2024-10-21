from django.db import models
# Create your models here.


class Qualifications(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    img = models.ImageField(verbose_name='Картинка', upload_to='static/img/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Квалификации'
        verbose_name_plural = 'Квалификации'


class FAQ(models.Model):
    title = models.CharField(verbose_name='Вопрос', max_length=50)
    content = models.TextField(verbose_name='Содержание', max_length=500)

    def __str__(self):
        return self.title
