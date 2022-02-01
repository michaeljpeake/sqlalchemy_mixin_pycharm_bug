from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry

# SQLAlchemy 1.4 style
mapper_registry = registry()
Base = mapper_registry.generate_base()

# SQLAlchemy 1.3 style
# Base = declarative_base()


class MyMixin:
    created_utc = Column(DateTime(timezone=True), server_default=func.timezone("UTC", func.statement_timestamp()))


class MyOtherMixin:
    pass


class MyModel(MyMixin, Base):
    another_field = Column(String)


class MyMoreBasicModel(MyOtherMixin, Base):
    only_field = Column(String)


example = MyModel(another_field="This should not cause a warning")
example_2 = MyMoreBasicModel(only_field="This should not cause a warning")
