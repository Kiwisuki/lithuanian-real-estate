import logging

from sqlalchemy.orm import Session
from sqlalchemy.sql import select

from parsing_job.database.schemas import ScrapedHtml

LOGGER = logging.getLogger(__name__)

def get_scraped_data(db_session: Session, acceptable_object_types: list[str]) -> dict[str, list[ScrapedHtml]]:
    """Get the scraped data grouped by object type."""
    scraped_data = db_session.execute(
        select(ScrapedHtml)
        .where(ScrapedHtml.object_type.in_(acceptable_object_types)),
    ).scalars().all()
    result = {}
    for scraped_html in scraped_data:
        if scraped_html.object_type not in result:
            result[scraped_html.object_type] = []
        result[scraped_html.object_type].append(scraped_html)
    return result


