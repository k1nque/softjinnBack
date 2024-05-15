from django.db import models
from django.contrib.auth.models import User
import uuid


class wishes(models.Model):
    wish_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name="Название", null=False)
    description = models.TextField(verbose_name="Описание")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Идея"
        verbose_name_plural = "Идеи"


class wishes_to_implements(models.Model):
    wish_to_implementer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wish_id = models.ForeignKey(wishes, verbose_name="Идентификатор идеи", on_delete=models.CASCADE, null=False)
    implementer_username = models.ForeignKey(
        User, verbose_name="Пользователь-реализатор", on_delete=models.CASCADE, null=False
    )
    implementation_link = models.URLField(null=True)

    def __str__(self) -> str:
        return f'{self.wish_id}: {self.implementer_username}'

    class Meta:
        verbose_name = "Идея-Реализатор"
        verbose_name_plural = "Идеи-Реализаторы"
