def post(id: int):
    return {
        "username": f"test{id}",
        "password": f"test{id}",
        "email": f"test{id}@test.com",
        "first_name": f"test{id}",
        "last_name": f"test{id}",
    }
