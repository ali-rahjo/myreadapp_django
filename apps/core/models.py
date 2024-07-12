from django.db import models

# Create your models here.

class CreateModifiedAbstratct(models.Model):
    # this should default to the current date and time
    created_at = models.DateTimeField(
        auto_now_add=True, null=True)
    # this shuold be change each time a row is modified
    modified_at = models.DateTimeField(
        auto_now=True, null=True)

    class Meta:
        abstract = True

        