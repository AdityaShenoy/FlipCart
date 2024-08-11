def post(id: int):
    return {
        "name": f"test{id}",
        "description": f"test{id}",
        "price": id,
        "mrp": id,
    }
