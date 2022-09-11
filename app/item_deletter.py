from db.db_session import create_session
from item_finder import find_item_by_id, find_children


def delete_item(item):
    children = find_children(item.id)
    if not children is None:
        for child in children:
            delete_item(child)
    session = create_session()
    session.delete(item)
    session.commit()


def delete_item_by_id(id: str) -> bool:
    item = find_item_by_id(id)
    if item is None:
        return False
    delete_item(item)
    return True
