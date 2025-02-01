import logging
from uuid import UUID

from sqlalchemy.orm import Session

from flat_processing_job.database.schemas import ParsedFlat, RawListingHtml
from flat_processing_job.parser.parse_html import parse_flat_html
from flat_processing_job.parser.pydantic_models import Parsed

LOGGER = logging.getLogger(__name__)


def pyd_to_orm(parsed_data: Parsed, html_orm: RawListingHtml, object_type: str) -> ParsedFlat:
    """Insert parsed data into the database."""
    return ParsedFlat(
        price=parsed_data.price,
        address=parsed_data.address,
        house_number=parsed_data.main_info.house_number,
        apartment_number=parsed_data.main_info.apartment_number,
        area=parsed_data.main_info.area,
        room_count=parsed_data.main_info.room_count,
        floor=parsed_data.main_info.floor,
        total_floors=parsed_data.main_info.total_floors,
        year=parsed_data.main_info.year,
        building_type=parsed_data.main_info.building_type,
        heating=parsed_data.main_info.heating,
        condition=parsed_data.main_info.condition,
        energy_class=parsed_data.main_info.energy_class,
        features=parsed_data.main_info.features,
        additional_rooms=parsed_data.main_info.additional_rooms,
        additional_equipment=parsed_data.main_info.additional_equipment,
        security=parsed_data.main_info.security,
        description=parsed_data.description,
        nearest_kindergarten=parsed_data.distances.nearest_kindergarten,
        nearest_school=parsed_data.distances.nearest_school,
        nearest_store=parsed_data.distances.nearest_store,
        images=parsed_data.images,
        coordinates=parsed_data.coordinates,
        is_map_accurate=parsed_data.is_map_accurate,
        scraped_html_id=html_orm.html_id,
        object_type=object_type,
        url=html_orm.url,
    )


def parse_and_store_flat(
    html_orm: RawListingHtml,
    object_type: str,
    db_session: Session,
):
    """Parse and store the HTML content."""
    try:
        parsed_data = parse_flat_html(html_orm.html_content)
    except AttributeError:
        LOGGER.error(f"Failed to parse HTML content for {html_orm.html_id}")
        return
    parsed_flat = pyd_to_orm(parsed_data, html_orm, object_type)
    db_session.add(parsed_flat)
    db_session.commit()
    LOGGER.info(f"Stored parsed data for {html_orm.html_id}")
