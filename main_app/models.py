from django.db import models
import uuid

class users(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, verbose_name="Имя пользователя")


class wishes(models.Model):
    wish_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name="Название", null=False)
    description = models.TextField(verbose_name="Описание")


class wishes_to_implements(models.Model):
    wish_to_implementer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wish_id = models.ForeignKey(wishes, on_delete=models.CASCADE, null=False)
    implementer_id = models.ForeignKey(users, on_delete=models.CASCADE, null=False)

