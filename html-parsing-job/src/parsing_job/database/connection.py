from typing import Tuple

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session, sessionmaker

from parsing_job.database import DATABASE_URI, Base


def get_engine_and_session(database_url: str = DATABASE_URI) -> Tuple[Engine, Session]:
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session()
