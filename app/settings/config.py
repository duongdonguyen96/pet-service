import logging
import os
from datetime import datetime

import pytz

APPLICATION = {
    "version": "1.0.0",
    "project_name": os.getenv("PROJECT_NAME", "FastAPI Project"),
    "secret_key": os.getenv("SECRET_KEY", ""),
    "debug": bool(os.getenv("DEBUG", "") if os.getenv("DEBUG", "") in ["True", "true", "1"] else False),
    "allowed_hosts": list(os.getenv("ALLOWED_HOSTS", ["*"])),
}

# Read time zone from environment variable, default to 'Asia/Ho_Chi_Minh' if not set
TIME_ZONE = pytz.timezone(os.getenv('TIME_ZONE', 'Asia/Ho_Chi_Minh'))


class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt=None):
        dt = datetime.fromtimestamp(record.created, tz=TIME_ZONE)  # or use your desired timezone
        return dt.strftime(datefmt or self.default_time_format)


logger = logging.getLogger()
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = CustomFormatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
