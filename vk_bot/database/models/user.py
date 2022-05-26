from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    vk_id = fields.BigIntField()
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255)
    char = fields.CharField(max_length=100)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "vk_users"
