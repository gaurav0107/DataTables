from django.db import models

from common.models import TimeStampedModel


class AmplifyUser(TimeStampedModel):
    username = models.CharField(max_length=80, unique=True)
    email_id = models.CharField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=30)
    is_account_active = models.BooleanField(default=1)

    class Meta:
        db_table = 'amplify_user'
