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
        verbose_name = _("Раздел")
        verbose_name_plural = _("Раздел")
        ordering = ['title', ]