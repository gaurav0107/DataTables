from django.db import models


class TimeStampedModel(models.Model):
    """Abstract Base Class Model for created_at and last_updated
     at Datetime Fields"""

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
