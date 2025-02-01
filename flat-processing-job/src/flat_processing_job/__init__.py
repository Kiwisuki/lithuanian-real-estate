import logging

LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] - <%(name)s> - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)

try:
    from dotenv import load_dotenv

    assert load_dotenv(), "No .env file found, have you copied .env.tmpl to .env?"
    LOGGER.info("Loaded .env file.")
except ImportError:
    LOGGER.warning(
        "python-dotenv not installed, skipping .env loading, this is expected if running via Docker.",
    )

import os

LOGGER.info(f"{os.environ['DATABASE_URI']}")
