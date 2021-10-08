from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


def upload_to(instance, filename):
    return 'food/{}'.format(filename)


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, verbose_name=_('name'))

    def __str__(self):
        return self.name


class Foods(models.Model):
    name = models.CharField(max_length=250, verbose_name=_('name'))
    description = models.CharField(max_length=800, verbose_name=_('description'))
    price = models.IntegerField(verbose_name=_('price'))
    discount = models.IntegerField(verbose_name=_('discount'),blank=True,null=True)
    published = models.DateTimeField(auto_now_add=True, verbose_name=_('create time'))
    modified_time = models.DateTimeField(auto_now=True, verbose_name=_('modified time'))
    available = models.BooleanField(verbose_name=_('available'), default=True)
    total_price = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_to, null=True, blank=True, default='food/default.png',
                              validators=[FileExtensionValidator(
                                  allowed_extensions=('jpg', 'jpeg', 'mp4', 'wmv', 'flv', 'png'))]
                              ,verbose_name=_('image'))
    likes = models.ForeignKey(User, related_name='like', blank=True, null=True, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='category', verbose_name=_('category'), on_delete=models.CASCADE
                                ,default=0 )

    class Meta:
        db_table = _('food')
        verbose_name = _('food')
        verbose_name_plural = _('foods')
        ordering = ['-published']

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        if self.discount:
            total = (self.discount * self.price) / 100
            return int(self.price - total)
        elif not self.discount:
            return int(self.price)
        return self.total_price
