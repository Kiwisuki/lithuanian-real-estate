import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.sql import func

from parsing_job.database import Base


class ScrapedHtml(Base):

    """Model for storing scraped HTML content."""

    __tablename__ = "scraped_html"
    html_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date_scraped = Column(DateTime, default=func.now())
    object_type = Column(String, nullable=False)
    url = Column(String, nullable=False)
    html_content = Column(String, nullable=True)


class ParsedFlat(Base):
    __tablename__ = "parsed_flats"

    parsed_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    price = Column(String, nullable=False)
    house_number = Column(String, nullable=True)
    apartment_number = Column(String, nullable=True)
    area = Column(String, nullable=True)
    room_count = Column(String, nullable=True)
    floor = Column(String, nullable=True)
    total_floors = Column(String, nullable=True)
    year = Column(String, nullable=True)
    building_type = Column(String, nullable=True)
    heating = Column(String, nullable=True)
    condition = Column(String, nullable=True)
    energy_class = Column(String, nullable=True)
    features = Column(String, nullable=True)
    additional_rooms = Column(String, nullable=True)
    additional_equipment = Column(String, nullable=True)
    security = Column(String, nullable=True)
    description = Column(String, nullable=False)
    nearest_kindergarten = Column(String, nullable=True)
    nearest_school = Column(String, nullable=True)
    nearest_store = Column(String, nullable=True)
    images = Column(JSONB, nullable=False)  # JSONB type to store list of image URLs
    coordinates = Column(
        JSONB, nullable=False,
    )  # JSONB type to store list of coordinates
    is_map_accurate = Column(Boolean, nullable=False)
    data_parsed = Column(DateTime, default=func.now())

    # Foreign key to the ScrapedHtml table
    scraped_html_id = Column(
        UUID(as_uuid=True), nullable=False,
    )
    object_type = Column(String, nullable=False)
