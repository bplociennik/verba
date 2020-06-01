from django.db import models
from django.utils.translation import gettext_lazy as _


class Sentence(models.Model):
    word = models.ForeignKey(
        "words.Word", on_delete=models.CASCADE, related_name="sentences"
    )
    name = models.CharField(_("name"), max_length=200)

    class Meta:
        verbose_name = _("sentence")
        verbose_name_plural = _("sentences")

    def __str__(self):
        return f"Sentence ({self.id})"
