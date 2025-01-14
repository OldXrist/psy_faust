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


class Services(models.Model):
    title = models.CharField(verbose_name='Название услуги', max_length=22)
    time = models.IntegerField(verbose_name='Продолжительность сессии')
    price = models.IntegerField(verbose_name='Стоимость услуги', max_length=5)
    desc = models.CharField(verbose_name='Описание', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class FAQ(models.Model):
    title = models.CharField(verbose_name='Вопрос', max_length=150)
    content = models.TextField(verbose_name='Содержание', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class Contacts(models.Model):
    telegram = models.CharField(verbose_name='Telegram', max_length=50)
    whatsapp = models.CharField(verbose_name='Whatsapp', max_length=50)
    email = models.CharField(verbose_name='EMail', max_length=50)
    phone = models.CharField(verbose_name='Телефон', max_length=50)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
