from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField


class Category(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)
    title = models.CharField(_("Название"), max_length=1000, default='')
    content = RichTextField("Описание", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Разделы")
        verbose_name_plural = _("Разделы")
        ordering = ['title', ]


class Item(models.Model):
    title = models.CharField(_("Название объекта"), max_length=1000, default='')
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    content = RichTextField("Описание", blank=True)

    class Meta:
        verbose_name = _("Объект")
        verbose_name_plural = _("Объекты")
        ordering = ['num', 'title', ]

    def __str__(self):
        return self.title