
def post_add_obj(name, price, sellerId, contacts, like, view_count):
    data = {
        "name": name,
        "price": price,
        "sellerId": sellerId,
        "statistics": {
            "contacts": contacts,
            "like": like,
            "viewCount": view_count
        }
    }
    return data
