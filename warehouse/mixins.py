from django.db import models
from django.contrib import admin
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

class TimestampMixin(models.Model):
    """
    this mixin will automatically add created and modified record to models
    that are inherits from it. created is creation time of record in database
    modified is last modification time of record in database
    """
    created = models.DateTimeField(
        _("Created"),
        auto_now_add=True,
        help_text=_("Automatic insertion of record"
                    "time in database.")
    )
    modified = models.DateTimeField(
        _("modified"),
        auto_now=True,
        help_text=_("Automatic modification of record"
                    "time in database.")
    )

    class Meta:
        abstract = True