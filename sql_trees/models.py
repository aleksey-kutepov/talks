from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///:memory:', echo=True)

Base = declarative_base()


association_table = Table(
    'association', Base.metadata,
    Column('parent_id', Integer, ForeignKey('naive_tree.id')),
    Column('child_id', Integer, ForeignKey('naive_tree.id'))
)


class NaiveTree(Base):
    __tablename__ = 'naive_tree'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship('Child', secondary='association',
                            back_populates='parents')

