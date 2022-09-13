from service.db.db_session import create_session
from service.db.item import Item, TypeEnum


def find_item_by_id(id: str):
    session = create_session()
    item = session.query(Item).filter(Item.id == id).first()
    if not item:
        return None
    return item


def find_children(id: str):
    session = create_session()
    children = session.query(Item).filter(Item.parentId == id)
    if not children.first():
        return None
    return children


def serialize_file(item):
    return {
        "id": item.id,
        "url": item.url,
        "type": "FILE",
        "parentId": item.parentId,
        "date": item.date,
        "size": item.size,
        "children": None
    }


def calculate_size(item):
    children = find_children(item.id)
    ans = 0
    for child in children:
        if child.type == TypeEnum.FILE:
            ans += child.size
        else:
            ans += calculate_size(child)
    return ans


def serialize_folder(item):
    return {
        "id": item.id,
        "url": item.url,
        "type": "FOLDER",
        "parentId": item.parentId,
        "date": item.date,
        "size": calculate_size(item),
        "children": [serialize_file(child) if child.type == TypeEnum.FILE else serialize_folder(child) for child in
                     find_children(item.id)]
    }


def get_item_by_id(id: str):
    item = find_item_by_id(id)
    if item is None:
        return False
    if item.type == TypeEnum.FILE:
        return serialize_file(item)
    else:
        return serialize_folder(item)
