from django.db import models


class News(models.Model):
    title = models.CharField(max_length=250, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контект')
    created_ed = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_ed = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_ed']
