import os
from pydantic import BaseSettings
import logging

logger = logging.getLogger(__name__)


class Settings(BaseSettings):
    asyncpg_url: str = os.getenv("SQL_DB", "postgresql+asyncpg://bwcelvdd:uwjUQ68ABrTdaqwVLXpOtgDHxDNWvPGd@kesavan.db.elephantsql.com/bwcelvdd")
    host: str = os.getenv("host_redis", "redis-18027.c98.us-east-1-4.ec2.cloud.redislabs.com")
    port: int = os.getenv("port_redis", 18027)
    password: str = os.getenv("password_redis", "rvQRG3d1KsGElUhGgxanebrx1soeYUfm")
    repeat_event: int = os.getenv("repeat_event", 30)    

