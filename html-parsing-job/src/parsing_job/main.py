import logging
from typing import List

from parsing_job import ALL_OBJECT_TYPES
from parsing_job.database.connection import get_engine_and_session
from parsing_job.database.retrieval import get_scraped_data
from parsing_job.parser.html_to_db import parse_and_store_flat

LOGGER = logging.getLogger(__name__)


def parsing_job(
    object_types_to_parse: List[str] = ALL_OBJECT_TYPES,
) -> None:
    """Scrape the Aruodas website."""
    engine, session = get_engine_and_session()
    scraped_ids = get_scraped_data(session, object_types_to_parse)
    for object_type, html_data in scraped_ids.items():
        for html_orm in html_data:
            parse_and_store_flat(html_orm, object_type, session)
    session.close()
    engine.dispose()


if __name__ == "__main__":
    parsing_job()
