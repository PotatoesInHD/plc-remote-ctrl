import os
import sys
import logging
from configparser import NoOptionError, NoSectionError

from config import Config
from logger_cfg import Logger
from exceptions import FatalConfigError

cfg: Config

logger = logging.getLogger(__name__)


def initialize_logger() -> tuple[str, Logger]:
    log_instance = Logger()
    log_path: str = log_instance.setup_logger()
    return (log_path, log_instance)


def initialize_config():
    global cfg        # setup config, exit if fails
    try:
        cfg = Config()
    except (NoSectionError, NoOptionError) as err:
        logger.warning(f"Error in Config.ini file: {err}", exc_info=True)
        sys.exit(1)
    except FatalConfigError as err:
        logger.warning(f"Error: {err}")
        sys.exit(1)
    except Exception as err:
        logger.warning(f"Error in Config.ini file: {err}", exc_info=True)
        sys.exit(1)


def main():
    log_path, log_instance = initialize_logger()
    initialize_config()


if __name__ == "__main__":
    main()
