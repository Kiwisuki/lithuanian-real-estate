from sqlalchemy.orm import DeclarativeBase
import os
DATABASE_URI = os.environ["DATABASE_URI"]


class Base(DeclarativeBase):

    """Base class for all SQLAlchemy models."""
