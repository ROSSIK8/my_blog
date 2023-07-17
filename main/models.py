from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название')
    image = models.CharField(max_length=1000)
    text = models.TextField(null=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-id']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=256,
                             verbose_name='Название',
                             null=True)
    articles = models.ManyToManyField(Article,
                                      related_name='category')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
