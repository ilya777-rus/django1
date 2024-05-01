from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=77, verbose_name='Название категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(max_length=555, verbose_name='Краткое описание')
    full_description = models.TextField(verbose_name="Полное описание")
    image = models.ImageField(upload_to='uploads/posts', blank=True, null=True, verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title