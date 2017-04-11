from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
from mptt.models import MPTTModel, TreeForeignKey
from ckeditor.fields import RichTextField
from embed_video.fields import EmbedVideoField
from sorl.thumbnail import ImageField

REALTY_CHOICES = (
    (0, 'Нет'),
    (1, 'В аренде'),
    (2, 'В собственности'),
)


class Category(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)
    title = models.CharField(_("Название"), max_length=1000, default='')
    content = RichTextField("Описание", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Раздел")
        verbose_name_plural = _("Разделы")
        ordering = ['title', ]

class Reg(models.Model):
    created_date = models.DateTimeField(_("Дата создания"), auto_now_add=True, editable=False)
    edited_date = models.DateTimeField(_("Дата редактирования"), auto_now=True, editable=False, null=True)
    title = models.CharField(_("Наименование"), max_length=1000, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Регион")
        verbose_name_plural = _("Регионы")
        ordering = ['title', ]


class Item(models.Model):
    title = models.CharField(_("Название объекта"), max_length=1000, default='')
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    regions = models.ForeignKey(Reg, on_delete=models.CASCADE, blank=True, null=True)

    fio = models.CharField(_("Контактное лицо"), max_length=1000, default='')
    phone = models.CharField(_("Телефон"), max_length=12, default='')
    email = models.EmailField(_("E-mail"), max_length=30, default='')
    purchase =  models.DecimalField(_("Стоимость"), max_digits=10, decimal_places=2, blank=True, null=True)
    receipts =  models.DecimalField(_("Выручка"), max_digits=10, decimal_places=2, blank=True, null=True)
    profit =  models.DecimalField(_("Прибыль"), max_digits=10, decimal_places=2, blank=True, null=True)
    costs =  models.DecimalField(_("Расходы"), max_digits=10, decimal_places=2, blank=True, null=True)
    borrowed =  models.DecimalField(_("Заемные средства"), max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(_("Товарный остаток"), max_digits=10, decimal_places=2, blank=True, null=True)
    part = models.CharField(_("Доля"), max_length=12, default='')
    age = models.CharField(_("Возраст"), max_length=12, default='')
    staff = models.CharField(_("Персонал"), max_length=12, default='')
    means = models.CharField(_("Средства производства"), max_length=2000, default='')
    licenses = models.CharField(_("Лицензии и сертификаты"), max_length=1000, default='')
    realty = models.IntegerField(_("Недвижимость"), choices=REALTY_CHOICES, default=0)








    content = RichTextField("Описание", blank=True)







    class Meta:
        verbose_name = _("Объект")
        verbose_name_plural = _("Объекты")
        ordering = ['num', 'title', ]

    def __str__(self):
        return self.title

class ItemPhoto(models.Model):
    file = ImageField(_("Изображение"), upload_to='gallery', blank=True)
    youtube_url = EmbedVideoField(_("Youtube адрес видео"), blank=True)
    num = models.IntegerField(_("Порядковый номер"), default=0, blank=True, db_index=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")
        ordering = ['num', ]

    def __str__(self):
        return 'изображение'
