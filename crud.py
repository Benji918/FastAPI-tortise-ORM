from models import TestUser

async def create_user(username: str, password: str, email: str):
    try:
        user = await TestUser.create(username=username, password=password, email=email)
        return user
    except Exception as e:
        return {"error": str(e)}


async def read_user(username: str, password: str):
    try:
        user = await TestUser.get(username=username, password=password)
        return user
    except Exception as e:
        return {"error": str(e)}

async def get_all_users():
    try:
        users = await TestUser.all()
        return users
    except Exception as e:
        return {"error": str(e)}

