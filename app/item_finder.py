from db.db_session import create_session
from db.item import Item


def find_item_by_id(id: str):
    session = create_session()
    item = session.query(Item).filter(Item.id == id)
    if not item:
        return None
    return item


def find_children(id: str):
    session = create_session()
    children = session.query(Item).filter(Item.parentId == id)
    if not children:
        return None
    return children


def get_node_by_id(id: str) -> dict:
    session = create_session()
    item = session.query(Item).filter(Item.id == id)
    ans = {
        "id": item.id,
        "url": item.url,
        "type": item.type,
        "parentId": item.parentId,
        "date": item.date,
        "size": item.size,
    }
    children = []
    for child in session.query(Item).filter(Item.parentId == id):
        children.append(get_node_by_id(child.id))
    if children:
        ans["children"] = children
    else:
        ans["children"] = "null"
    return ans
