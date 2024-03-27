from django.db import models



class NewModel(models.Model):
    news = models.CharField("Категория", max_length=30, db_index=True)
    news_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news

    class Meta:
        verbose_name = 'Article category'
        verbose_name_plural = 'Article categories'


class TagModel(models.Model):
    tag_title = models.CharField("Тэг", max_length=30, help_text='Тут добавьте Тэг')

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class NewsModel(models.Model):
    news_title = models.CharField("Название статьи", max_length=100, help_text='Тут добавьте название статьи')
    news_categories = models.ForeignKey(NewModel, verbose_name="Article categories",
                                           on_delete=models.CASCADE, null=True)
    news_tags = models.ManyToManyField(TagModel, verbose_name="Tag", default='')
    news_news = models.TextField("Статья")
    news_image = models.FileField("Изображение", upload_to='article_images')
    news_author = models.CharField("Автор", max_length=50, help_text='ФИО автора')
    news_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news_title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


