from tortoise import Model, fields

class TestUser(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20)
    password = fields.CharField(max_length=100)
    email = fields.CharField(max_length=50)
    token = fields.CharField(max_length=100, null=True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "test_users"
    
    def __str__(self):
        return self.username