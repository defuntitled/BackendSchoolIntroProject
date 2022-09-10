import enum
import sqlalchemy
from sqlalchemy import orm
from db_session import SqlalchemyBase
from datetime import datetime


class TypeEnum(enum.Enum):
    FILE = 1
    FOLDER = 2


class Item(SqlalchemyBase):
    __tablename__ = "items"
    item_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, unique=True, autoincrement=True)
    parent_item_id = sqlalchemy.Column(sqlalchemy.ForeignKey('items.item_id', ondelete='CASCADE', onupdate='CASCADE'),
                                       index=True)
    id = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    url = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now(), nullable=False)
    parentId = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    type = sqlalchemy.Column(sqlalchemy.Enum(TypeEnum), nullable=True)
    children = orm.relationship("Item", remote_side=[item_id])
