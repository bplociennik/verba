from django.db import models
from django.utils.translation import ugettext_lazy as _

from config.utils import upload_to_classname


class Word(models.Model):
    name = models.CharField(_("name"), max_length=50, unique=True)
    description = models.TextField(_("description"), blank=True, default="")

    audio = models.ImageField(
        _("audio"), blank=True, null=True, upload_to=upload_to_classname
    )
    image = models.ImageField(
        _("image"), blank=True, null=True, upload_to=upload_to_classname
    )

    created = models.DateTimeField(_("created"), auto_now_add=True)
    modified = models.DateTimeField(_("modified"), auto_now=True)

    class Meta:
        verbose_name = _("word")
        verbose_name_plural = _("words")

    def __str__(self):
        return f"Word ({self.name})"
