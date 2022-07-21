import os
from pydantic import BaseSettings
import logging

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    asyncpg_url: str = os.getenv("SQL_DB", "postgresql+asyncpg://bwcelvdd:uwjUQ68ABrTdaqwVLXpOtgDHxDNWvPGd@kesavan.db.elephantsql.com/bwcelvdd")
