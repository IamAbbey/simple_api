from uuid import uuid4

from django.db import models


class UUIDData(models.Model):

    generated_uuid = models.UUIDField(default=uuid4)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "UUIDData"
        verbose_name_plural = "UUIDData"
        ordering = ["-created_date"]

    def __str__(self):
        return f"{self.generated_uuid}"
