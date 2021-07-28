from django.db import models


class ArticleModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    content = models.TextField(verbose_name='Статья')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)


class CommentModel(models.Model):
    email = models.EmailField(verbose_name='Email комментатора')
    name = models.CharField(max_length=200, verbose_name='Имя')
    text = models.TextField(verbose_name='Комментарии')
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True, default=0,related_name='comments_app')
    article = models.ForeignKey(ArticleModel, verbose_name='Статья', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.name} {self.email}'